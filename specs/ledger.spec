%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:             ledger
Version:          3.3.2
Release:          %autorelease
Summary:          A powerful command-line double-entry accounting system
License:          BSD-3-Clause
URL:              https://ledger-cli.org/
Source0:          https://github.com/ledger/ledger/archive/v%{version}.tar.gz
Patch0:           ledger-boost190.patch

BuildRequires:    boost-devel
BuildRequires:    cmake
BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    gettext-devel
BuildRequires:    gmp-devel
BuildRequires:    libedit-devel
BuildRequires:    mpfr-devel
BuildRequires:    utf8cpp-devel

# For building documentation.
BuildRequires:    doxygen
BuildRequires:    graphviz
BuildRequires:    man2html
BuildRequires:    texinfo
BuildRequires:    texlive-cm-super
BuildRequires:    texlive-ec
BuildRequires:    texlive-eurosym
BuildRequires:    texinfo-tex

%description
Ledger is a powerful, double-entry accounting system that is accessed
from the UNIX command-line. This may put off some users — as there is
no flashy UI — but for those who want unparalleled reporting access to
their data, there really is no alternative.

%package devel
Summary: Libraries and header files for %{name} development
Requires: %{name} = %{version}-%{release}
%description devel
Libraries and header files for %{name} development.

%prep
%autosetup -n %{name}-%{version} -p1
# Avoid texinfo errors on EL7.
%if 0%{?rhel} == 7
sed -i -e 's#FIXME:UNDOCUMENTED#FIXMEUNDOCUMENTED#g' doc/ledger3.texi
%endif
rm -r lib/utfcpp


%build
%cmake \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DCMAKE_SKIP_RPATH:BOOL=ON \
       -DUSE_PYTHON:BOOL=OFF \
       -DUSE_DOXYGEN:BOOL=ON \
       -DBUILD_WEB_DOCS:BOOL=ON

%cmake_build
%cmake_build -t doc

%install
%cmake_install

# Bash completion
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d
install -p -m0644 contrib/ledger-completion.bash \
    %{buildroot}%{_sysconfdir}/bash_completion.d/ledger

# Install documentation manually to a convenient directory layout
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_infodir}/*

# Info files
cp -p %{__cmake_builddir}/doc/ledger3.info* %{buildroot}%{_infodir}

# Contrib scripts
mkdir -p %{buildroot}%{_pkgdocdir}/contrib
for i in bal bal-huquq compilation-ledger.el entry getquote.pl getquote-uk.py ledger-du README repl.sh report tc ti to trend; do
    install -p -m0644 contrib/${i} %{buildroot}%{_pkgdocdir}/contrib/${i}
done

# Input samples
mkdir -p %{buildroot}%{_pkgdocdir}/samples
for i in demo.ledger divzero.dat drewr3.dat drewr.dat sample.dat standard.dat transfer.dat wow.dat; do
    install -p -m0644 test/input/${i} %{buildroot}%{_pkgdocdir}/samples/${i}
done

# Tests are disabled for the time being since they seem to require Python 2
#%%check
# Tests all fail when removing rpath.
#LD_LIBRARY_PATH=$PWD %%ctest

%files
%doc README.md doc/GLOSSARY.md NEWS.md
%doc %{__cmake_builddir}/doc/ledger3.html
%doc %{__cmake_builddir}/doc/ledger3.pdf
# https://bugzilla.redhat.com/show_bug.cgi?id=728959
# These must be explicitly listed.
%doc %{_pkgdocdir}/contrib
%doc %{_pkgdocdir}/samples
%{_bindir}/ledger
%{_infodir}/ledger3.info*
%{_libdir}/libledger.so.3
%{_mandir}/man1/ledger.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/ledger
%license LICENSE.md

%files devel
%{_includedir}/ledger
%{_libdir}/libledger.so


%changelog
%autochangelog
