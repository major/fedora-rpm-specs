Name:        iverilog
Version:     13.0
%global uver 13_0
Release:     %autorelease
Summary:     Icarus Verilog is a verilog compiler and simulator

License:     GPL-2.0-only
URL:         https://github.com/steveicarus/iverilog
Source0:     https://github.com/steveicarus/iverilog/archive/%{name}-%{uver}.tar.gz

BuildRequires: autoconf
BuildRequires: bzip2-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: gperf
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: readline-devel
BuildRequires: zlib-devel
# python3-sphinx is needed to build the documentation
BuildRequires: python3-sphinx


%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.


%package devel
Summary:     Header files for Icarus Verilog development
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files needed to develop VPI/PLI modules
for Icarus Verilog.


%package static
Summary:     Static libraries for Icarus Verilog development
Requires:    %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains the static libraries needed to develop VPI/PLI modules
for Icarus Verilog.


%prep
%autosetup -n %{name}-%{uver}
# Clean junk files from tarball
find . -name .git -exec rm -rf {} +
find . -name autom4te.cache -exec rm -rf {} +


%build
%configure
%make_build

# Build Sphinx documentation as well
%make_build -C Documentation html
rm -f Documentation/_build/html/.buildinfo


%install
%make_install INSTALL="install -p"


%check
make check


%files
%license COPYING
%doc README.md examples Documentation/_build/html
%{_bindir}/iverilog
%{_bindir}/iverilog-vpi
%{_bindir}/vvp
%{_libdir}/ivl
%{_mandir}/man1/*


%files devel
%{_includedir}/iverilog/


%files static
%{_libdir}/*.a


%changelog
%autochangelog
