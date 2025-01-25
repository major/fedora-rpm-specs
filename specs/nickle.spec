%if 0%{?fedora}
%bcond_without docs
%else
# rubygem dependencies not in EPEL yet
%bcond_with docs
%endif

Name:           nickle
Version:        2.102
Release:        %autorelease
Summary:        A programming language-based prototyping environment

License:        MIT
URL:            https://nickle.org
Source0:        https://nickle.org/release/nickle-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
%if %{with docs}
# for documentation
BuildRequires:  rubygem(asciidoctor-pdf)
BuildRequires:  rubygem(prawn-icon)
BuildRequires:  rubygem(prawn-svg)
%endif

%description
Nickle is a programming language based prototyping environment with
powerful programming and scripting capabilities. Nickle supports a
variety of datatypes, especially arbitrary precision numbers. The
programming language vaguely resembles C. Some things in C which do
not translate easily are different, some design choices have been made
differently, and a very few features are simply missing.

Nickle provides the functionality of UNIX bc, dc and expr in
much-improved form. It is also an ideal environment for prototyping
complex algorithms. Nickle's scripting capabilities make it a nice
replacement for spreadsheets in some applications, and its numeric
features nicely complement the limited numeric functionality of
text-oriented languages such as AWK and PERL.

%package devel
Summary:  Include files for Nickle
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Include files for Nickle, used for building external FFI (foreign
function interface) libraries (e.g. the Cairo interface for Nickle).


%prep
%autosetup -p1


%build
autoreconf -fiv

%if 0%{?fedora} >= 42
# gram.y has Bool bool, bool is a reserved keyword in C23
# https://gcc.gnu.org/gcc-15/porting_to.html
export CFLAGS="%{optflags} -std=gnu17"
%endif

# we will install documentation ourselves,
# but this saves having to delete the ones installed by 'make install'
%configure --docdir=%{_pkgdocdir}
%make_build


%check
cd test
make check


%install
%make_install DESTDIR=$RPM_BUILD_ROOT
rm `find examples -name 'Makefile*'`
rm examples/COPYING


%files
%license COPYING
%doc README README.name AUTHORS TODO debian/changelog
%doc examples
%if %{with docs}
%doc doc/tutorial/nickle-tutorial.pdf
%endif
%{_bindir}/nickle
%{_datadir}/nickle/
%exclude %{_datadir}/nickle/COPYING
%exclude %{_datadir}/nickle/examples
%{_mandir}/man1/nickle.1*

%files devel
%{_includedir}/nickle

%changelog
%autochangelog
