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
%bcond acceptance_ruby 1

Name:           gherkin
Version:        39.0.0
# While SONAME versions are based on the major version number, we repeat them
# here as a reminder, hopefully reducing the chance of an unintended SONAME
# version bump.
%global cpp_soversion 39
%global c_soversion 39
Release:        %autorelease
Summary:        A parser and compiler for the Gherkin language

License:        MIT
URL:            https://github.com/cucumber/gherkin
Source:         %{url}/archive/v%{version}/gherkin-%{version}.tar.gz

# Man pages hand-written for Fedora in groff_man(7) format based on --help
Source10:       gherkin.1
Source11:       gherkin-cpp.1
Source12:       gherkin-ruby.1

# Update cmake_minimum_required for C to 3.12; support CMake 4
# https://github.com/cucumber/gherkin/pull/546
Patch:          %{url}/pull/546.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# For “unbundling” gherkin-languages.json from the Python library
BuildRequires:  symlinks

# For both C and C++:
BuildRequires:  cmake
# C++ library has "LANGUAGES C CXX" in CMake, so it still needs a C compiler
BuildRequires:  gcc

%if %{with acceptance_c} || \
    %{with acceptance_cpp} || \
    %{with acceptance_python} || \
    %{with acceptance_ruby}
BuildRequires:  make
BuildRequires:  jq
%endif

# For C++ only:
BuildRequires:  gcc-c++
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(cucumber_messages) >= 31

# For Python only:
BuildRequires:  python3-devel
# The “dev” dependency group contains test dependencies intermixed with
# unwanted dependencies for coverage analysis
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# pre-commit, etc., so we list test dependencies manually.
BuildRequires:  %{py3_dist pytest}

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


# We package the RubyGem as a subpackage, rather than as a separate
# rubygem-cucumber-gherkin source package based on the relesed Gem archive,
# because having the full gherkin source code makes it much easier to run
# acceptance tests and to keep the RubyGem up to date and synchronized with
# other languages’ implementations without duplication of effort.
#
# The Ruby specific content is kept as close as feasible to the output of
# `gem2rpm --fetch cucumber-gherkin`.

%global gem_name cucumber-gherkin

%package -n rubygem-cucumber-gherkin
Summary:        Gherkin parser
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel >= 3.2.8
BuildRequires:  ruby >= 3.2
BuildRequires:  rubygem(cucumber-messages)
BuildRequires:  rubygem(rspec)
BuildArch:      noarch

%description -n rubygem-cucumber-gherkin
%{summary}.


%package -n rubygem-cucumber-gherkin-doc
Summary: Documentation for rubygem-cucumber-gherkin
Requires: rubygem-cucumber-gherkin = %{version}-%{release}
BuildArch: noarch

%description -n rubygem-cucumber-gherkin-doc
%{summary}.


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
# Python: We must work with what we have, and compatibility is quite good in
# practice.
%pyproject_patch_dependency uv_build:drop_upper


%generate_buildrequires
%pyproject_buildrequires -d python


%conf
echo '==== Configuring C implementation ===='
pushd c
%cmake
popd

echo '==== Configuring C++ implementation ===='
pushd cpp
%cmake
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
%pyproject_wheel -d python

echo '==== Building Ruby implementation ===='
pushd ruby
gem build %{gem_name}.gemspec
%gem_install
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
# Avoid conflict: both C++ and Ruby try to provide /usr/bin/gherkin.
# Because Ruby was the original implementation, use it for /usr/bin/gherkin.
mv '%{buildroot}%{_bindir}/gherkin' '%{buildroot}%{_bindir}/gherkin-cpp'
# Since F45, no longer install gherkin-generate-tokens. It is not clear if this
# is intended for users, or only for acceptance testing. In any case, there may
# be conflicts across language implementations as there are for the gherkin
# executable; Ruby has a gherkin-generate-tokens, but it isn’t installed by
# default. We can reconsider this, hopefully with a better understanding of the
# full picture, if it turns out that something actually needs this.
rm '%{buildroot}%{_bindir}/gherkin-generate-tokens'

echo '==== Installing Python implementation ===='
%pyproject_install
%pyproject_save_files -l gherkin
ln -s -f %{buildroot}%{_datadir}/gherkin/gherkin-languages.json \
    '%{buildroot}%{python3_sitelib}/gherkin/gherkin-languages.json'
symlinks -c -o '%{buildroot}%{python3_sitelib}/gherkin/gherkin-languages.json'

echo '==== Installing Ruby implementation ===='
pushd ruby
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
# Allow Ruby to provide /usr/bin/gherkin, since the Ruby implementation was the
# original.
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f -executable \
    -exec chmod -v a-x '{}' '+'
popd


echo '==== Installing man pages ===='
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'


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
# The executables need to load libcucumber_gherkin, so we also set
# LD_LIBRARY_PATH. The acceptance tests are not safe for parallel execution.
LD_LIBRARY_PATH='%{buildroot}%{_libdir}' %make_build -j1 acceptance \
    GHERKIN='%{_vpath_builddir}/src/bin/gherkin/gherkin' \
    GHERKIN_GENERATE_TOKENS='%{_vpath_builddir}/src/bin/gherkin-generate-tokens/gherkin-generate-tokens'
%endif
popd

echo '==== Testing Python implementation ===='
%pyproject_check_import
%pytest python/tests
%if %{with acceptance_python}
# Override the generator script commands so that they don’t use “uv run”; we
# don’t want a dependency on uv, and we can’t respect uv.lock or download
# dependencies from the network.
%{py3_test_envvars} %make_build -C python acceptance \
    GHERKIN_GENERATE_EVENTS='%{python3} scripts/generate_events.py' \
    GHERKIN_GENERATE_TOKENS='%{python3} scripts/generate_tokens.py'
%endif

echo '==== Testing Ruby implementation ===='
pushd ruby
ln -r -s spec .%{gem_instdir}/spec
ln -r -s ../testdata .%{gem_instdir}/../testdata
pushd .%{gem_instdir}
rspec -rspec_helper spec
popd
%if %{with acceptance_ruby}
# Keep make from trying to rebuild the Ruby implemention
mkdir -p .built
touch Gemfile.lock
# Override commands so that they don’t use “bundle”; we don’t want a dependency
# on bundle, and we can’t respect Gemfile.lock or download dependencies from
# the network.
%make_build acceptance \
    GHERKIN='ruby bin/gherkin' \
    GHERKIN_GENERATE_TOKENS='ruby bin/gherkin-generate-tokens'
%endif
popd


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
%{_bindir}/gherkin-cpp
%{_mandir}/man1/gherkin-cpp.1*


%files -n python3-gherkin-official -f %{pyproject_files}
%doc README.md


%files -n rubygem-cucumber-gherkin
%dir %{gem_instdir}
%{_bindir}/gherkin-ruby
%{_bindir}/gherkin
%{_mandir}/man1/gherkin.1*
%{_mandir}/man1/gherkin-ruby.1*
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}


%files -n rubygem-cucumber-gherkin-doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md


%changelog
%autochangelog
