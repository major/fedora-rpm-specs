# Header-only library
%global debug_package %{nil}

%global forgeurl https://github.com/taskflow/taskflow
Version: 3.4.0
%forgemeta

Name: taskflow
Release: %{autorelease}
# Most of the package is MIT
# taskflow/utility/uuid.hpp: BSL-1.0
# taskflow/core/notifier.hpp: MPL-2.0
# None of the files in 3rd-party/ or sandbox/ are present in the binary RPM
License: MIT and BSL-1.0 and MPL-2.0
Summary: Header library for writing parallel and heterogeneous with C++
URL: https://taskflow.github.io/
Source: %{name}-%{version}-norefpdfs.tar.gz
# This script is used to generate the source tarball actually used by the Fedora
# package from the upstream sources. The upstream source contains a number of
# publication PDFs with ambiguous or prohibited license terms. Since some of the
# terms limiting "posted to a server for redistribution", not even the source
# tarball stored by Fedora should contain the files.
Source1: generate-tarball.sh

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doctest-devel

%global _description %{expand:
Taskflow is a C++ header library which helps you quickly write parallel and
heterogeneous task programs with high performance and simultaneous high
productivity. It is faster, more expressive, fewer lines of code, and easier
for drop-in integration than many of existing task programming libraries. }

%description %_description

%package devel
Summary: Development files for the Taskflow library
Provides: taskflow-static = %{version}-%{release}

%description devel
%_description

%package doc
Summary: Documentation for the Taskflow library
BuildArch: noarch

%description doc
%_description

%prep
%autosetup
# Safety check to help make sure PDFs don't sneak their way into the package.
pdfs=$(find -name "*.pdf")
if [ -n "$pdfs" ]; then
    echo "PDFs should not be present due to license terms!"
    exit 1
fi

# Most of these bundled libraries are only used by code in sandbox/, thus the
# bundled code can be removed.
rm -fr 3rd-party
# doctest is used by unittests, but point to the system version instead
sed -i \
    -e 's,include(.*/doctest.cmake),include(%{_libdir}/cmake/doctest/doctest.cmake),' \
    -e 's,\${TF_3RD_PARTY_DIR}/doctest,%{_includedir}/doctest,' \
    unittests/CMakeLists.txt

%build
%cmake
%cmake_build
# Rename the html docs directory to html, so that the naming when included in
# /usr/share/ makes more sense.
mv docs html
# Change the links from local PDF references (which have been removed from the
# source tarball) to point to the GitHub page. This way they aren't
# redistributed in the Fedora package, but the links aren't broken.
sed -i 's,href="\([^/]\+\.pdf\)",href="%{forgeurl}/raw/v%{version}/docs/\1",g' \
    html/*.html
# Remove the intermediate xml files used to generate the html docs.
rm -rf html/xml

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/taskflow
%{_libdir}/cmake/Taskflow

%files doc
%license LICENSE
%doc examples
%doc html

%changelog
%autochangelog
