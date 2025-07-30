# Implementations for various other languages are present in the source. Some,
# like Dart, belong to ecosystems that are not packaged. Others, like Perl,
# could perhaps be enabled if motivation existed. Still others should be (or
# already are) separate source packages, like:
# - golang-github-cucumber-gherkin
# - rubygem-cucumber-gherkin

# Run acceptance tests?
%bcond acceptance_c 1
%bcond acceptance_cpp 1
%bcond acceptance_python 1

Name:           gherkin
Version:        33.1.0
# While SONAME versions are based on the major version number, we repeat them
# here as a reminder, hopefully reducing the chance of an unintended SONAME
# version bump.
%global cpp_soversion 33
%global c_soversion 33
Release:        %autorelease
Summary:        A parser and compiler for the Gherkin language

License:        MIT
URL:            https://github.com/cucumber/gherkin
Source:         %{url}/archive/v%{version}/gherkin-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format: gherkin.1 is based
# on “gherkin --help”, and gherkin-generate-tokens.1 is written from scratch
# based on a cursory inspection of gherkin-generate-tokens.cpp.
Source10:       gherkin.1
Source11:       gherkin-generate-tokens.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# For “unbundling” gherkin-languages.json from the Python library
BuildRequires:  symlinks

# For both C and C++:
BuildRequires:  cmake
# Faster than the "UNIX Makefiles" cmake backend, with no disadvantages
BuildRequires:  ninja-build
# C++ library has "LANGUAGES C CXX" in CMake, so it still needs a C compiler
BuildRequires:  gcc

%if %{with acceptance_c} || %{with acceptance_cpp} || %{with acceptance_python}
BuildRequires:  make
BuildRequires:  jq
%endif

# For C++ only:
BuildRequires:  gcc-c++
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(cucumber_messages)

# For Python only:
BuildRequires:  python3-devel

%global common_description %{expand:
Gherkin is a parser and compiler for the Gherkin language.}

%description %{common_description}


%package data
Summary:        Data files shared among multiple Gherkin implementations

BuildArch:      noarch

%description data %{common_description}

This package contains data files shared among multiple Gherkin implementations.


%package c-libs
Summary:        Libraries implementing Gherkin in C

# This does not depend on gherkin-data; instead, the contents of
# c/src/dialect.c are *derived from* gherkin-languages.json.

%description c-libs %{common_description}

This package contains libraries implementing Gherkin in C.


%package c-devel
Summary:        Development files for using the C implementation of Gherkin

Requires:       %{name}-c-libs%{?_isa} = %{version}-%{release}

%description c-devel %{common_description}

This package contains header files and libraries for developing and building
programs that use the C implementation of Gherkin.


%package cpp-libs
Summary:        Libraries implementing Gherkin in C++

# This does not depend on gherkin-data; instead, the contents of
# cpp/src/lib/gherkin/cucumber/gherkin/dialect.cpp are *derived from*
# gherkin-languages.json.

%description cpp-libs %{common_description}

This package contains libraries implementing Gherkin in C++.


%package cpp-devel
Summary:        Development files for using the C++ implementation of Gherkin

Requires:       %{name}-cpp-libs%{?_isa} = %{version}-%{release}

%description cpp-devel %{common_description}

This package contains header files and libraries for developing and building
programs that use the C++ implementation of Gherkin.


%package cpp-tools
Summary:        Command-line tools associated with the C++ implementation of Gherkin

Requires:       %{name}-cpp-libs%{?_isa} = %{version}-%{release}

%description cpp-tools %{common_description}

This package contains command-line tools associated with the C++ implementation
of Gherkin.


# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming
# The canonical project name is gherkin-official; the PyPI project is
# https://pypi.org/project/gherkin-official.
%package -n python3-gherkin-official
Summary:        Gherkin parser (official, by Cucumber team)

BuildArch:      noarch

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
#
# There is a namespace conflict with https://pypi.org/project/gherkin/, but
# that project has been unmaintained for more than 15 years and is unlikely to
# ever be packaged.
%py_provides python3-gherkin

Requires:       gherkin-data = %{version}-%{release}

%description -n python3-gherkin-official %{common_description}


%prep
%autosetup -n gherkin-%{version} -p1

# Tweaks for running acceptance tests
#
# C: Don’t try to rebuild the (C) CLI; we want to use the one already built
# with CMake. This is easier than trying to convince make that the targets in
# question have already been built, which is the strategy we follow for the C++
# acceptance tests.
sed -r -i 's/^(\.run:) cli \$\(GHERKIN\)/\1/' c/Makefile
# Python: Fix unversioned python interpreter.
sed -r -i 's@python -m@%{python3} -m@' python/Makefile



%generate_buildrequires
pushd python >/dev/null
%pyproject_buildrequires requirements.txt
popd >/dev/null


%conf
echo '==== Configuring C implementation ===='
pushd c
%cmake -GNinja
popd

echo '==== Configuring C++ implementation ===='
pushd cpp
%cmake -GNinja
popd


%build
echo '==== Building C implementation ===='
pushd c
%cmake_build
popd

echo '==== Building C++ implementation ===='
pushd cpp
%cmake_build
popd

echo '==== Building Python implementation ===='
pushd python
%pyproject_wheel
popd


%install
install -t '%{buildroot}%{_datadir}/gherkin' -D -p -m 0644 \
    gherkin-languages.json

echo '==== Installing C implementation ===='
pushd c
%cmake_install
popd

echo '==== Installing C++ implementation ===='
pushd cpp
%cmake_install
popd
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}'

echo '==== Installing Python implementation ===='
pushd python
%pyproject_install
%pyproject_save_files -l gherkin
ln -s -f %{buildroot}%{_datadir}/gherkin/gherkin-languages.json \
    '%{buildroot}%{python3_sitelib}/gherkin/gherkin-languages.json'
symlinks -c -o '%{buildroot}%{python3_sitelib}/gherkin/gherkin-languages.json'
popd


%check
echo '==== Testing C implementation ===='
pushd c
# C tests are automatically executed during %%cmake_build.
%if %{with acceptance_c}
# Keep make from trying to rebuild the C implementation.
touch .built
# The executables need to load libgherkin, so we also set LD_LIBRARY_PATH. We
# could omit this since copies of the libraries are in %%{_vpath_builddir}
# alongside the executables, but we might as well use the copies in the
# buildroot, as we do for the C++ acceptance tests.
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %make_build acceptance \
    GHERKIN='%{_vpath_builddir}/gherkinexe' \
    GHERKIN_GENERATE_TOKENS='%{_vpath_builddir}/gherkin_generate_tokens'
%endif
popd

echo '==== Testing C++ implementation ===='
pushd cpp
# We think this is the intended way to run tests, but there don’t appear to be
# any usable tests yet.
%ctest
%if %{with acceptance_cpp}
# Keep make from trying to rebuild the C++ implementation or invoke cmate.
mkdir -p .built
# While there are GHERKIN/GHERKIN_GENERATE_TOKENS variables in the Makefile,
# symlinking the already-built command-line tools in ./stage/bin is the easiest
# way to make sure the acceptance tests can run them.
mkdir -p stage
ln -s '%{buildroot}%{_bindir}' stage/bin
# The executables need to load libcucumber_gherkin, so we also set
# LD_LIBRARY_PATH. The acceptance tests are not safe for parallel execution.
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %make_build -j1 acceptance
%endif
popd

echo '==== Testing Python implementation ===='
%pyproject_check_import
%pytest
%if %{with acceptance_python}
%{py3_test_envvars} %make_build -C python acceptance
%endif


%files data
%license LICENSE
%doc CHANGELOG.md
%doc MARKDOWN_WITH_GHERKIN.md
%doc README.md

%dir %{_datadir}/gherkin
%{_datadir}/gherkin/gherkin-languages.json


%files c-libs
%license LICENSE
%{_libdir}/libgherkin.so.%{c_soversion}{,.*}


%files c-devel
%doc c/README.md
# Co-owned with packages for other cucumber projects:
%dir %{_includedir}/cucumber/
# Unique to this package:
%dir %{_includedir}/cucumber/gherkin/
%{_includedir}/cucumber/gherkin/*.h

%{_libdir}/libgherkin.so
%{_libdir}/cmake/gherkin/


%files cpp-libs
%license LICENSE
%{_libdir}/libcucumber_gherkin.so.%{cpp_soversion}{,.*}


%files cpp-devel
%doc cpp/README.md
# https://github.com/cucumber/messages/issues/267#issuecomment-2478224301
# Co-owned with packages for other cucumber projects:
%dir %{_includedir}/cucumber/
# Co-owned with packages for other cucumber projects in the cucumber C++
# namespace:
%dir %{_includedir}/cucumber/cucumber/
# Unique to this package:
%dir %{_includedir}/cucumber/cucumber/gherkin/
%{_includedir}/cucumber/cucumber/gherkin/*.hpp

%{_libdir}/libcucumber_gherkin.so
%{_libdir}/cmake/cucumber_gherkin/


%files cpp-tools
%{_bindir}/gherkin
%{_bindir}/gherkin-generate-tokens
%{_mandir}/man1/gherkin.1*
%{_mandir}/man1/gherkin-generate-tokens.1*


%files -n python3-gherkin-official -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
