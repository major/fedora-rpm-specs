# NOTE: perl support was dropped in version 1.4.3.  It is available here:
# https://github.com/jelmer/subunit-perl

# Disable the tests in a bootstrap situation
%bcond bootstrap 0

Name:           subunit
Version:        1.4.5
Release:        %autorelease
Summary:        C bindings for subunit

%global majver  %(cut -d. -f-2 <<< %{version})
%global giturl  https://github.com/testing-cabal/subunit

License:        Apache-2.0 OR BSD-3-Clause
URL:            https://launchpad.net/subunit
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  python3-devel

%if %{without bootstrap}
BuildRequires:  pkgconfig(check)
%endif

# This can be removed when F43 reaches EOL
Obsoletes:      %{name}-perl < 1.4.3

%description
Subunit C bindings.  See the python-subunit package for test processing
functionality.

%package devel
Summary:        Header files for developing C applications that use subunit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for developing C applications that use subunit.

%package cppunit
Summary:        Subunit integration into cppunit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description cppunit
Subunit integration into cppunit.

%package cppunit-devel
Summary:        Header files for applications that use cppunit and subunit
Requires:       %{name}-cppunit%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       cppunit-devel%{?_isa}

%description cppunit-devel
Header files and libraries for developing applications that use cppunit
and subunit.

%package shell
Summary:        Shell bindings for subunit
BuildArch:      noarch

%description shell
Subunit shell bindings.  See the python-subunit package for test
processing functionality.

%package -n python3-%{name}
Summary:        Streaming protocol for test results
BuildArch:      noarch

# This can be removed when Fedora 41 reaches EOL
Obsoletes:      python2-%{name} < 1.4.1

%description -n python3-%{name}
Subunit is a streaming protocol for test results.  The protocol is a
binary encoding that is easily generated and parsed.  By design all the
components of the protocol conceptually fit into the xUnit TestCase ->
TestResult interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell.  Bindings are easy to
write for other languages.

A number of useful things can be done easily with subunit:
- Test aggregation: Tests run separately can be combined and then
  reported/displayed together.  For instance, tests from different
  languages can be shown as a seamless whole.
- Test archiving: A test run may be recorded and replayed later.
- Test isolation: Tests that may crash or otherwise interact badly with
  each other can be run separately and then aggregated, rather than
  interfering with each other.
- Grid testing: subunit can act as the necessary serialization and
  deserialization to get test runs on distributed machines to be
  reported in real time.

%package -n python3-%{name}-test
Summary:        Test code for the python 3 subunit bindings
BuildArch:      noarch
Requires:       python3-%{name} = %{version}-%{release}
Requires:       %{name}-filters = %{version}-%{release}

%description -n python3-%{name}-test
%{summary}.

%package filters
Summary:        Command line filters for processing subunit streams
BuildArch:      noarch
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3-gobject
Requires:       gtk3 >= 3.20
Requires:       libnotify >= 0.7.7
Requires:       %{py3_dist junitxml}

%description filters
Command line filters for processing subunit streams.

%package static
Summary:        Static C library for subunit
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Subunit C bindings in a static library, for building statically linked
test cases.

%prep
%autosetup -p1

%conf
fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

# Fix underlinked library
sed "/^tests_LDADD/ilibcppunit_subunit_la_LIBADD = -lcppunit libsubunit.la\n" \
    -i Makefile.am

# Do not use env
for fil in $(grep -Frl "%{_bindir}/env python"); do
  sed -ri.orig 's,%{_bindir}/env python3?,%{python3},' $fil
  fixtimestamp $fil
done

# Update an obsolete autoconf macro
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' configure.ac

%if %{with bootstrap}
# We do not run tests in bootstrap mode, so don't look for check
sed -i '/PKG_CHECK_MODULES.*CHECK/d' configure.ac
%endif

# Generate the configure script
autoreconf -fi

%generate_buildrequires
%pyproject_buildrequires -x docs%{!?with_bootstrap:,test}

%build
# Build for python3
export PYTHON=%{_bindir}/python3
%configure --enable-shared --enable-static

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build
%pyproject_wheel

%install
%pyproject_install
chmod 0755 %{buildroot}%{python3_sitelib}/%{name}/run.py
chmod 0755 %{buildroot}%{python3_sitelib}/%{name}/tests/sample-script.py
chmod 0755 %{buildroot}%{python3_sitelib}/%{name}/tests/sample-two-script.py

# We set pkgpython_PYTHON for efficiency to disable automake python compilation
%make_install pkgpython_PYTHON='' INSTALL="%{_bindir}/install -p"

# Install the shell interface
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cp -p shell/share/%{name}.sh %{buildroot}%{_sysconfdir}/profile.d

# Fix permissions
chmod 0755 %{buildroot}%{python3_sitelib}/%{name}/filter_scripts/*.py
chmod 0644 %{buildroot}%{python3_sitelib}/%{name}/filter_scripts/__init__.py
chmod 0755 %{buildroot}%{python3_sitelib}/%{name}/tests/sample-script.py
chmod 0755 %{buildroot}%{python3_sitelib}/%{name}/tests/sample-two-script.py

# Fix timestamps
touch -r c/include/%{name}/child.h %{buildroot}%{_includedir}/%{name}/child.h
touch -r c++/SubunitTestProgressListener.h \
      %{buildroot}%{_includedir}/%{name}/SubunitTestProgressListener.h

%check
%if %{without bootstrap}
# Run the tests for python3
export LD_LIBRARY_PATH=$PWD/.libs
export PYTHON=%{python3}
make check
%endif

%files
%doc NEWS README.md
%license Apache-2.0 BSD COPYING
%{_libdir}/lib%{name}.so.0{,.*}

%files devel
%doc c/README
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/child.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files cppunit
%{_libdir}/libcppunit_%{name}.so.0{,.*}

%files cppunit-devel
%doc c++/README
%{_includedir}/%{name}/SubunitTestProgressListener.h
%{_libdir}/libcppunit_%{name}.so
%{_libdir}/pkgconfig/libcppunit_%{name}.pc

%files shell
%doc shell/README
%license Apache-2.0 BSD COPYING
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.sh

%files -n python3-%{name}
%license Apache-2.0 BSD COPYING
%{python3_sitelib}/%{name}/
%{python3_sitelib}/python_%{name}-%{version}.dist-info/
%exclude %{python3_sitelib}/%{name}/tests/

%files -n python3-%{name}-test
%{python3_sitelib}/%{name}/tests/

%files static
%{_libdir}/*.a

%files filters
%{_bindir}/subunit*
%{_bindir}/tap2subunit

%changelog
%autochangelog
