Summary:	Optimizer for png files
Summary(pl):	Optymalizator plik�w png
Summary(pt_BR):	Utilit�rio para compress�o de pngs
Name:		optipng
Version:	0.4.8
Release:	1
License:	zlib/libpng
Group:		Applications/Graphics
Source0:	http://www.cs.toronto.edu/~cosmin/pngtech/optipng/%{name}-%{version}.tar.gz
# Source0-md5:	0f3648f06a389d7bbb1e6bf309581b6a
URL:		http://www.cs.toronto.edu/~cosmin/pngtech/optipng/
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main purpose of OptiPNG is to *optimize* PNG files, i.e. to reduce
their size to a minimum, without losing any information. In order to
achieve this goal, OptiPNG performs the following tasks:

- It losslessly reduces the bit depth, the color type and the color
  palette of the image. This step reduces the size of the uncompressed
  image, which, indirectly, reduces the size of the compressed image
  (i.e. the size of the PNG file).

- It runs a suite of compression methods and strategies, and selects
  the compression parameters that yield the smallest output file.

%description -l pl
G��wnym zadaniem OptiPNG jest optymalizacja plik�w PNG, tzn.
zmniejszenie ich rozmiaru do minimum bez straty jakichkolwiek
informacji. Aby osi�gn�� ten cel stosuje si�:

- Bezstratn� redukcj� g��bi kolor�w, typu koloru i palety kolor�w. Ten
  krok zmniejsza rozmiar nieskompresowanego obrazu, przez co zmniejsza
  si� r�wnie� rozmiar skompresowanego obrazu (czyli wielko�� pliku PNG).

- Por�wnuje si� wyniki dzia�ania r�nych metod i strategii kompresji w
  celu wyboru takich parametr�w, kt�re daj� najmniejszy rozmiar pliku
  wynikowego.

%prep
%setup -q

%build
%{__make} -C src -f scripts/gcc.mak \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/optipng $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/*
