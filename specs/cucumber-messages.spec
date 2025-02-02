# Re-generate sources? The results should be identical to what is already in
# the source archive. Each language has its own conditional here:
%bcond regenerate_cpp 1
%bcond regenerate_python 1

# Run tests that require network access? We cannot do this routinely in koji,
# but we can do it manually by enabling this conditional and enabling network
# access, e.g. in COPR, or in a local mock chroot:
#   fedpkg mockbuild --with network_tests --enable-network
%bcond network_tests 0

Name:           cucumber-messages
Version:        27.2.0
%global cpp_soversion 27
Release:        %autorelease
Summary:        A message protocol for representing results and other information from Cucumber

License:        MIT
URL:            https://github.com/cucumber/messages
Source:         %{url}/archive/v%{version}/messages-%{version}.tar.gz

# Add a LICENSE file for Python
# https://github.com/cucumber/messages/pull/278
# Just the commit with the file, not the one that adds a changelog entry:
Patch:          %{url}/pull/278/commits/509e51ca1f7bea03b45f3e89146d291735db57ec.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
# Faster than the "UNIX Makefiles" cmake backend, with no disadvantages
BuildRequires:  ninja-build

BuildRequires:  gcc-c++
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  cmake(nlohmann_json) json-static

%if %{with regenerate_cpp} || %{with regenerate_python}
BuildRequires:  make
BuildRequires:  /usr/bin/ruby
BuildRequires:  rubygem(json)
%endif

# Python test dependencies; the "test" and "test-coverage" extras have a lot of
# extra dependencies that are unwanted per
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters,
# so we list these manually.
BuildRequires:  %{py3_dist pytest}
%if %{with network_tests}
BuildRequires:  %{py3_dist GitPython}
%endif

%global common_description %{expand:
Cucumber Messages is a message protocol for representing results and other
information from Cucumber. The protocol aims to decouple various components of
the Cucumber platform, with the following advantages:

  • Each component only needs to know about a subset of messages
  • Gherkin is decoupled from the Cucumber execution component
  • Enables the future support other formats such as Markdown and Excel}

%description %{common_description}


%package cpp-libs
Summary:        Cucumber Messages for C++ (JSON schema)

%description cpp-libs %{common_description}

This package contains libraries implementing Cucumber Messages for C++.


%package cpp-devel
Summary:        Development files for using the C++ implementation of Gherkin

Requires:       %{name}-cpp-libs%{?_isa} = %{version}-%{release}

%description cpp-devel %{common_description}

This package contains header files and libraries for developing and building
programs that use Cucumber Messages for C++.


# Please publish the new Python bindings on PyPI
# https://github.com/cucumber/messages/issues/277
%package -n python3-cucumber-messages
Summary:        Message protocol for representing results and other information from Cucumber

BuildArch:      noarch

%description -n python3-cucumber-messages
Cucumber Messages is a message protocol for representing results and other
information from Cucumber.


%prep
%autosetup -n messages-%{version} -p1


%generate_buildrequires
pushd python >/dev/null
%pyproject_buildrequires
popd >/dev/null


%conf
pushd cpp
%cmake -GNinja
popd


%build
pushd cpp
%if %{with regenerate_cpp}
%make_build clean
%make_build generate
%endif
%cmake_build
popd

pushd python
%if %{with regenerate_python}
%make_build clean
%make_build generate
%endif
%pyproject_wheel
popd


%install
pushd cpp
%cmake_install
popd

pushd python
%pyproject_install
%pyproject_save_files -l cucumber_messages
popd


%check
pushd cpp
# We think this is the intended way to run tests, but there don’t appear to be
# any usable tests yet.
%ctest
popd

pushd python
%if %{without network_tests}
# Requires network access (remote git clone):
ignore="${ignore-} --ignore=tests/test_model_load.py"
%endif
%pytest ${ignore-} -v
popd


%files cpp-libs
%license LICENSE
%{_libdir}/libcucumber_messages.so.%{cpp_soversion}{,.*}


%files cpp-devel
%doc cpp/README.md
# https://github.com/cucumber/messages/issues/267#issuecomment-2478224301
# Co-owned with packages for other cucumber projects:
%dir %{_includedir}/cucumber/
# Co-owned with packages for other cucumber projects in the cucumber C++
# namespace:
%dir %{_includedir}/cucumber/cucumber/
# Unique to this package:
%dir %{_includedir}/cucumber/cucumber/messages/
%{_includedir}/cucumber/cucumber/messages/*.hpp

%{_libdir}/libcucumber_messages.so
%{_libdir}/cmake/cucumber_messages/


%files -n python3-cucumber-messages -f %{pyproject_files}
%doc python/README.md


%changelog
%autochangelog
