# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
%bcond doc 1

Name:           cpp-hocon
Version:        0.3.0
# Makes sure an SONAME bump does not catch us by surprise. Currently, there is
# no ABI stability even across patch releases, and the SONAME comes from the
# complete version number.
%global so_version 0.3.0
Release:        %autorelease
Summary:        C++ support for the HOCON configuration file format

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

License:        Apache-2.0
URL:            https://github.com/puppetlabs/cpp-hocon
Source:         %{url}/archive/%{version}/cpp-hocon-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
# Our choice; the make backend would work fine too
BuildRequires:  ninja-build

BuildRequires:  boost-devel
BuildRequires:  cmake(leatherman)
BuildRequires:  gettext

# Tests
BuildRequires:  catch1-devel

# Documentation
BuildRequires:  doxygen
%if %{with doc}
BuildRequires:  doxygen-latex
BuildRequires:  make
%endif

# See facter, which has the same workaround.
# autoreq is not picking this one up so be specific
Requires:       leatherman%{?_isa}

%description
This is a port of the TypesafeConfig library to C++.

The library provides C++ support for the HOCON configuration file format.


%package devel
Summary:        Development files for the cpp-hocon library
Requires:       cpp-hocon%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       leatherman-devel%{?_isa}

%description devel
Libraries and headers to link against cpp-hocon.


%if %{with doc}
%package doc
Summary:        Documentation for the cpp-hocon library

BuildArch:      noarch

%description doc
Documentation for the cpp-hocon library.
%endif


%prep
%autosetup

# Do not use the obsolete vendored copy of the Catch unit testing library
# included with leatherman.
sed -r -i 's/(LEATHERMAN_COMPONENTS)(\b.+)?(\bcatch\b)/\1\2/' CMakeLists.txt
sed -r -i 's|\$\{LEATHERMAN_CATCH_INCLUDE\}|"%{_includedir}/catch"|' \
    lib/tests/CMakeLists.txt

%if %{with doc}
# We enable the Doxygen PDF documentation as a substitute. We must enable
# GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and should
# already be set as we like them. We also disable GENERATE_HTML, since we will
# not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    lib/Doxyfile.in
%endif


%build
%cmake \
    -DLeatherman_DIR=%{_libdir}/cmake/leatherman \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -GNinja
%cmake_build

%if %{with doc}
pushd lib
doxygen Doxyfile
%make_build -C latex
mv latex/refman.pdf latex/cpp-hocon.pdf
popd
%endif


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%if %{without doc}
%doc README.md
%endif
%{_libdir}/libcpp-hocon.so.%{so_version}


%files devel
%{_libdir}/libcpp-hocon.so
%{_includedir}/hocon/


%if %{with doc}
%files doc
%license LICENSE
%doc lib/latex/cpp-hocon.pdf
%endif


%changelog
%autochangelog
