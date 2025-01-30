Name:           cucumber-messages
Version:        27.1.0
%global cpp_soversion 27
Release:        %autorelease
Summary:        A message protocol for representing results and other information from Cucumber

License:        MIT
URL:            https://github.com/cucumber/messages
Source:         %{url}/archive/v%{version}/messages-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
# Faster than the "UNIX Makefiles" cmake backend, with no disadvantages
BuildRequires:  ninja-build

BuildRequires:  gcc-c++
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
BuildRequires:  cmake(nlohmann_json) json-static

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


%prep
%autosetup -n messages-%{version} -p1


%conf
pushd cpp
%cmake -GNinja
popd


%build
pushd cpp
%cmake_build
popd


%install
pushd cpp
%cmake_install
popd


%check
pushd cpp
# We think this is the intended way to run tests, but there don’t appear to be
# any usable tests yet.
%ctest
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


%changelog
%autochangelog
