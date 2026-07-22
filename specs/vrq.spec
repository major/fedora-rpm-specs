Name:           vrq
Version:        1.0.134
Release:        %autorelease
Summary:        Verilog tool framework with plugins for manipulating source code
License:        GPL-2.0-or-later
URL:            https://vrq.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         vrq-gcc11.patch
Patch1:         vrq-non-x86.patch

BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  iverilog
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  man2html-core
BuildRequires:  perl-Time-HiRes
BuildRequires:  readline-devel
BuildRequires:  zlib-devel


%description
VRQ is modular verilog parser that supports plugin tools to process verilog. 
Multiple tools may be invoked in a pipeline fashion within a single execution 
of vrq. It is a generic front-end parser with support for plugin backend 
customizable tools.

%package devel
Summary:        Header files and libraries for Vrq development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The vrq-devel package contains the header files and libraries needed
to develop backend plugin customization tools for the vrq tool framework.

%prep
%autosetup -p1
find . -name CVS -exec rm -rf {} +
find . -name '*.o' -delete
find . -name '*.so' -delete

%build
export CXXFLAGS="-std=c++14 %{build_cxxflags}"
%configure
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -rf `find %{buildroot} -name latex`

# add some doc files into the buildroot manually (#992864)
for f in AUTHORS ChangeLog COPYING README doc/faq.html ; do
    install -p -m0644 -D $f %{buildroot}%{_docdir}/%{name}/${f}
done

install -d -m0755 %{buildroot}%{_docdir}/%{name}/doc
cp -pr doc/html %{buildroot}%{_docdir}/%{name}/doc

install -d -m0755 %{buildroot}%{_docdir}/%{name}/plugin
cp -pr plugin/examples %{buildroot}%{_docdir}/%{name}/plugin

rm -rf %{buildroot}%{_docdir}/%{name}-%{version}
%fdupes %{buildroot}%{_docdir}



%check
make check || :

%files
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/doc
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/README
%{_docdir}/%{name}/doc/faq.html
%{_bindir}/%{name}
%{_libdir}/%{name}-%{version}
%{_mandir}/man1/vrq.1.gz

%files devel
%{_docdir}/%{name}/doc/html
%{_docdir}/%{name}/plugin/examples
%{_includedir}/%{name}-%{version}

%changelog
%autochangelog

