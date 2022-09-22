# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

%global debug_package %{nil}

%global common_description %{expand:
Termcolor is a header-only C++ library for printing colored messages to the
terminal. Written just for fun with a help of the Force.

Termcolor uses ANSI color formatting, so you can use it on every system that is
used such terminals (most *nix systems, including Linux and Mac OS).}

Name:           termcolor
Version:        2.0.0
Release:        %autorelease
Summary:        Header-only C++ library for printing colored messages to the terminal

License:        BSD
URL:            https://github.com/ikalnytskyi/termcolor
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# https://github.com/ikalnytskyi/termcolor/pull/63
Patch0:         0001-Use-GNUInstallDirs-for-install-targets.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif

%description %{common_description}

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
Requires:  cmake-filesystem

%description devel %{common_description}

%package        doc
Summary:        Documentation and examples for %{name}
BuildArch:      noarch

%description    doc %{common_description}

%prep
%autosetup -p1

%build
%cmake -DTERMCOLOR_TESTS:BOOL=ON
%cmake_build

%if %{with doc_pdf}
sphinx-build -b latex docs %{_vpath_builddir}/_latex
%make_build -C %{_vpath_builddir}/_latex LATEXMKOPTS='-quiet'
%endif

%install
%cmake_install

# test_termcolor is a visual test
# It should show colors, but mock will show without colors.
%check
%{_vpath_builddir}/test_termcolor

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%files doc
%license LICENSE
%doc README.rst
%doc examples
%if %{with doc_pdf}
%doc %{_vpath_builddir}/_latex/termcolor.pdf
%endif

%changelog
%autochangelog
