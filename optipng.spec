Summary:	Optimizer for png files
Summary(pl):	Optymalizator plików png
Summary(pt_BR):	Utilitário para compressão de pngs
Name:		optipng
Version:	0.4.3
Release:	1
License:	zlib/libpng
Group:		Applications/Graphics
Source0:	http://www.cs.toronto.edu/~cosmin/pngtech/optipng/%{name}-%{version}.tar.gz
# Source0-md5:	3ed23ff9c204d7ffbd0fa6b3c53d830e
Patch0:		%{name}-opt.patch
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
G³ównym zadaniem OptiPNG jest optymalizacja plików PNG, tzn.
zmniejszenie ich rozmiaru do minimum bez straty jakichkolwiek
informacji. Aby osi±gn±æ ten cel stosuje siê:

- Bezstratn± redukcjê g³êbi kolorów, typu koloru i palety kolorów. Ten
  krok zmiejsza rozmiar nieskompresowanego obrazu, przez co zmniejsza
  siê równie¿ rozmiar skompresowanego obrazu (czyli wielko¶æ pliku PNG.)

- Porównuje siê wyniki dzia³ania ró¿nych metod i strategii kompresji w
  celu wyboru takich parametrów, które daj± najmniejszy rozmiar pliku
  wynikowego.

%prep
%setup -q
%patch0 -p1

%build
cd src
%{__make} -f scripts/Makefile.gcc \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I../zlib"

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
