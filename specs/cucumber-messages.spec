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
Version:        32.3.1
%global cpp_soversion 32
Release:        %autorelease
Summary:        A message protocol for representing results and other information from Cucumber

License:        MIT
URL:            https://github.com/cucumber/messages
Source:         %{url}/archive/v%{version}/messages-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
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


%package -n python3-cucumber-messages
Summary:        Message protocol for representing results and other information from Cucumber

BuildArch:      noarch

%description -n python3-cucumber-messages
Cucumber Messages is a message protocol for representing results and other
information from Cucumber.


%prep
%autosetup -n messages-%{version} -p1
# Do not upper-bound (SemVer-bound) the version of uv_build; we must work with
# what we have, and compatibility is quite good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' python/pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -d python


%conf
pushd cpp
%cmake
popd


%build
%if %{with regenerate_cpp}
%make_build -C cpp clean
%make_build -C cpp generate
%endif
pushd cpp
%cmake_build
popd

%if %{with regenerate_python}
%make_build -C python clean
%make_build -C python generate
%endif
%pyproject_wheel -d python


%install
pushd cpp
%cmake_install
popd

%pyproject_install
%pyproject_save_files -l cucumber_messages


%check
pushd cpp
# We think this is the intended way to run tests, but there don’t appear to be
# any usable tests yet.
%ctest
popd

%if %{without network_tests}
# Requires network access (remote git clone):
ignore="${ignore-} --ignore=tests/test_model_load.py"
%endif
%pytest ${ignore-} -v python/tests


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
