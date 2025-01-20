Name:           python-qemu-qmp
Version:        0.0.3
Release:        6%{?dist}
Summary:        QEMU Monitor Protocol library

License:        GPL-2.0-only AND LGPL-2.0-or-later
# NB:           qemu/qmp/legacy.py is GPLv2 only.
#               Everything else installed is LGPLv2+.
URL:            https://pypi.org/project/qemu.qmp
Source0:        %{pypi_source qemu.qmp}

BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3dist(avocado-framework)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global _description %{expand:
qemu.qmp is a QEMU Monitor Protocol (“QMP”) library written in Python,
using asyncio. It is used to send QMP messages to running QEMU
emulators. It requires Python 3.6+ and has no mandatory
dependencies. This library can be used to communicate with QEMU
emulators, the QEMU Guest Agent (QGA), the QEMU Storage Daemon (QSD), or
any other utility or application that speaks QMP.}

%description %_description

%package -n     python3-qemu-qmp
Summary:        %{summary}

%description -n python3-qemu-qmp %_description

%package        doc
Summary:        Documentation for the %{summary}

%description    doc %_description

This package provides offline HTML documentation for python3-qemu-qmp.


%prep
%autosetup -n qemu.qmp-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
PYTHONPATH=${PWD} sphinx-build-3 -b man docs man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
# Explicitly exclude the 'qmp-tui' script shim from rpm release.
#
# It is meant to be included with the 'tui' extras, which are not being
# packaged here at this time. Without the extras, this shim merely
# prints an error and exits.
rm %{buildroot}%{_bindir}/qmp-tui

install -Dpm 0644 man/*.1 -t %{buildroot}%{_mandir}/man1/

# Use PEP420 namespace name instead of package name:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%pyproject_save_files qemu


%check
%pyproject_check_import -e qemu.qmp.qmp_tui
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PYTHONDONTWRITEBYTECODE=1
export PATH="%{buildroot}%{_bindir}:${PATH}"
avocado --config avocado.cfg run tests/*.py


%files -n python3-qemu-qmp -f %{pyproject_files}
%license LICENSE LICENSE_GPL2
%doc README.rst
%{_bindir}/qmp-shell
%{_bindir}/qmp-shell-wrap
%{_mandir}/man1/qmp-shell.1*
%{_mandir}/man1/qmp-shell-wrap.1*


%files doc
%license LICENSE LICENSE_GPL2
%doc html


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 John Snow <jsnow@redhat.com> - 0.0.3-1
- Update to v0.0.3

* Mon Jul 17 2023 Python Maint <python-maint@redhat.com> - 0.0.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 John Snow <jsnow@redhat.com> - 0.0.2-1
- Initial package. Fixes rhbz#2112474
