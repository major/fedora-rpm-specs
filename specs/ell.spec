# headers-only library
%global debug_package %{nil}

Name:           ell
Version:        0
Release:        %autorelease
Summary:        Header-only C++ library to write EBNF grammars
ExcludeArch:    %{ix86}
License:        LGPL-3.0-or-later
URL:            http://code.google.com/p/ell/

# this pristine source is the result of:
# svn export -r r282 http://ell.googlecode.com/svn/trunk ell-20130617
# tar -cJvf ell-20130617.tar.xz ell-20130617
Source0:        ell-20130617.tar.xz

%description
Embedded LL library is pure-header library to write EBNF grammars as C++ code.
It eases the development of parser or similar applications, while removing the
need to write a lexer.

%package        devel
BuildArch:      noarch
Summary:        Development files for ELL

# to track the usage of this library
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{name}-devel is only required for building software that uses the ELL library.
Because ELL is a header-only library, there is no matching run-time package.

%prep
%setup -q -n ell-20130617

%build

# workaround to fix FTBFS, disable tests
#check
#export CFLAGS="%{optflags}"
#make test

%install
mkdir -p %{buildroot}%{_includedir}/ell
cp -pr libELL/Include/ell/*.h %{buildroot}%{_includedir}/ell

%files devel
%doc COPYING.LESSER
%dir %{_includedir}/ell
%{_includedir}/ell/*.h

%changelog
%autochangelog
