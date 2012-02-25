#
# Conditional build:
%bcond_with	system_libpng	# use system libpng (forces system zlib; not ready for libpng 1.5)
%bcond_with	system_zlib	# use system zlib (included one is slightly more aggressive)
#
%if %{with system_libpng}
%define	system_zlib	1
%endif
Summary:	Optimizer for png files
Summary(pl.UTF-8):	Optymalizator plików png
Summary(pt_BR.UTF-8):	Utilitário para compressão de pngs
Name:		optipng
Version:	0.6.4
Release:	1
License:	BSD, Zlib/libpng
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/optipng/%{name}-%{version}.tar.gz
# Source0-md5:	d6c10dd8d8f1d5b579221bc9cfbfbcb6
URL:		http://optipng.sourceforge.net/
%{?with_system_libpng:BuildRequires:	libpng-devel >= 1.4.1}
%{?with_system_zlib:BuildRequires:	zlib-devel >= 1.2.4}
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

%description -l pl.UTF-8
Głównym zadaniem OptiPNG jest optymalizacja plików PNG, tzn.
zmniejszenie ich rozmiaru do minimum bez straty jakichkolwiek
informacji. Aby osiągnąć ten cel stosuje się:

- Bezstratną redukcję głębi kolorów, typu koloru i palety kolorów. Ten
  krok zmniejsza rozmiar nieskompresowanego obrazu, przez co zmniejsza
  się również rozmiar skompresowanego obrazu (czyli wielkość pliku
  PNG).

- Porównuje się wyniki działania różnych metod i strategii kompresji w
  celu wyboru takich parametrów, które dają najmniejszy rozmiar pliku
  wynikowego.

%prep
%setup -q

%build
./configure \
	-prefix=%{_prefix} \
	%{?with_system_libpng:-with-system-libpng} \
	%{?with_system_zlib:-with-system-zlib}

%{__make} -C src -f scripts/gcc.mak -j1 \
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
%doc doc/{caveat.txt,history.txt,manual.html,png_optimization_guide.html,thanks.html,todo.txt}
%attr(755,root,root) %{_bindir}/optipng
