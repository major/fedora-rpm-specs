%bcond tests 1

Name:           python-wcwidth
Version:        0.2.13
Release:        %autorelease
Summary:        Measures number of Terminal column cells of wide-character codes

# part of the code is under HPND-Markus-Kuhn
License:        MIT AND HPND-Markus-Kuhn
URL:            https://github.com/jquast/wcwidth
Source:         %{pypi_source wcwidth}

# Don't use codecs.open on Python 3
# Avoids: DeprecationWarnings: codecs.open() is deprecated. Use open() instead.
# Fixes https://bugzilla.redhat.com/2368969
Patch:          https://github.com/jquast/wcwidth/pull/141.patch

BuildArch:      noarch

%description
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%package -n     python3-wcwidth
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-wcwidth
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%prep
%autosetup -p1 -n wcwidth-%{version}
# skip coverage checks
sed -i -e 's|--cov[^[:space:]]*||g' tox.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wcwidth

%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif

%files -n python3-wcwidth -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
