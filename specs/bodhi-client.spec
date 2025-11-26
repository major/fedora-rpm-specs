Name:           bodhi-client
Version:        25.11.2
Release:        %autorelease
Summary:        Bodhi client

License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/bodhi
Source0:        %{pypi_source bodhi_client}
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-sphinx

Requires: koji

Obsoletes: python3-bodhi-client <= 5.7.5
# Replace the bodhi metapackage
Obsoletes: bodhi <= 5.7.5

%py_provides python3-bodhi-client

%description
Command-line client for Bodhi, Fedora's update gating system.

%prep
%autosetup -n bodhi_client-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%make_build -C docs man

%install
%pyproject_install
# Poetry doesn't support PEP 639 yet, so we still need to manually mark the
# license file.
# https://github.com/python-poetry/poetry/issues/9670
%pyproject_save_files -L bodhi

install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/bodhi.1 %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm0644 bodhi-client.bash %{buildroot}%{_sysconfdir}/bash_completion.d/bodhi-client.bash

%check
%pyproject_check_import
%{pytest} -v

%files -f %{pyproject_files}
%license %{python3_sitelib}/bodhi_client-%{version}.dist-info/COPYING
%{_bindir}/bodhi
%{_mandir}/man1/bodhi.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/bodhi-client.bash

%changelog
%autochangelog
