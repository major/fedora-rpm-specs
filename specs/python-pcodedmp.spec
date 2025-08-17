Name:           python-pcodedmp
Summary:        VBA p-code disassembler
Version:        1.2.6
Release:        28%{?dist}
License:        GPL-3.0-or-later
URL:            https://github.com/bontchev/pcodedmp
VCS:            https://github.com/bontchev/pcodedmp
BuildArch:      noarch

%global srcname pcodedmp

# Bootstrap may be needed to break circular dependencies between
# python-pcodedmp and python-oletools
%bcond_with     bootstrap

# No python-pypandoc packages in EPEL 8 and 10 (yet?)
%if 0%{?fedora} || 0%{?rhel} == 9
%bcond_without  pypandoc
%else
%bcond_with     pypandoc
%endif

Source0:        %{pypi_source}



%global _description %{expand:
Macros written in VBA (Visual Basic for Applications; the macro programming
language used in Microsoft Office) exist in three different executable forms,
each of which can be what is actually executed at run time, depending on the
circumstances: Source code, p-code and execodes.

Since most of the time it is the p-code that determines what exactly a macro
would do (even if neither source code, nor execodes are present), pcodedmp is
a Python library and command line tool to display it.}

%description %_description

%package -n pcodedmp
Summary:        %{summary}
Requires:       python3-pcodedmp = %{version}-%{release}

%description -n pcodedmp %_description

%package -n python3-pcodedmp
Summary:        %{summary}
BuildRequires:  python3-devel
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  python3-setuptools
%endif
%if %{with pypandoc}
BuildRequires:  python3-pypandoc
%endif
%if %{without bootstrap}
BuildRequires:  python3-lxml
BuildRequires:  python3-oletools >= 0.54
Requires:       python3-oletools >= 0.54
%endif
%if 0%{?rhel} && 0%{?rhel} < 9
%{?python_provide:%python_provide python3-pcodedmp}
%endif

%description -n python3-pcodedmp %_description

%prep
%autosetup -n pcodedmp-%{version}

%if 0%{?fedora} || 0%{?rhel} >= 9
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_wheel
%else
%py3_build
%endif

%install
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_install
%pyproject_save_files -l pcodedmp
%else
%py3_install
%endif

# The check requires oletools, which might not be available during bootstrapping
%if %{without bootstrap}
%check
# There are no pytest tests defined at this moment
# %%pytest
%if 0%{?fedora} || 0%{?rhel} >= 9
%pyproject_check_import
%else
# Do at least basic smoke test
%py3_check_import pcodedmp
%endif
%endif

%files -n pcodedmp
%{_bindir}/pcodedmp

%if 0%{?fedora} || 0%{?rhel} >= 9
%files -n python3-pcodedmp -f %{pyproject_files}
%else
%files -n python3-pcodedmp
%license LICENSE
%{python3_sitelib}/pcodedmp/
%{python3_sitelib}/pcodedmp-*.egg-info/
%endif
%doc README.md

%changelog
* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.2.6-28
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

%autochangelog
