Name:        iverilog
Version:     13.0
%define uver 13_0
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


%prep
%autosetup -n %{name}-%{uver}
# Clean junks from tarball
find . -type f -name ".git" -exec rm '{}' \;
rm -rf `find . -type d -name "autom4te.cache" -exec echo '{}' \;`

%build
%configure
%make_build

# Build Sphinx documentation as well
%make_build -C Documentation html

 
%install
%{__make}    prefix=%{buildroot}%{_prefix} \
             bindir=%{buildroot}%{_bindir} \
             libdir=%{buildroot}%{_libdir} \
             libdir64=%{buildroot}%{_libdir} \
             includedir=%{buildroot}%{_includedir} \
             mandir=%{buildroot}%{_mandir}  \
             pdfdir=%{buildroot}%{_pdfdir}/ivl/ \
             vpidir=%{buildroot}%{_libdir}/ivl/ \
             INSTALL="install -p" \
install


# Install HTML documentation
rm -rf Documentation/_build/html/.buildinfo
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r Documentation/_build/html %{buildroot}%{_docdir}/%{name}

 
%check
make check
 
 
%files
%license COPYING
%doc examples html README.md
%{_bindir}/iverilog
%{_bindir}/iverilog-vpi
%{_bindir}/vvp
%{_libdir}/ivl
%{_mandir}/man1/*

# headers for PLI: This is intended to be used by the user.
%{_includedir}/*.h

# RHBZ 480531
%{_libdir}/*.a
 

%changelog
%autochangelog
