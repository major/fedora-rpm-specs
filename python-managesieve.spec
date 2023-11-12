%global pypi_name managesieve

# Pull from GitLab (prerequisite for Packit)
%global forgeurl https://gitlab.com/htgoebel/managesieve

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        %autorelease
Summary:        Accessing a Sieve-Server for managing Sieve scripts
%global tag v%{version}
%forgemeta
License:        PSF-2.0 AND GPL-3.0-only
URL:            https://managesieve.readthedocs.io/
Source0:        %forgesource
# ssl.wrap_socket is deprecated and Python 3.12 removed it entirely
# https://gitlab.com/htgoebel/managesieve/-/issues/8
Patch:          fix_ssl_wrap_socket_error.patch
BuildArch:      noarch

BuildRequires:  python3-devel, git-core
BuildRequires:  python3-pytest
BuildRequires:  make
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description
This module allows accessing a Sieve-Server for managing Sieve scripts there.
It is accompanied by a simple yet functional user application ‘sieveshell’.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
This module allows accessing a Sieve-Server for managing Sieve scripts there.
It is accompanied by a simple yet functional user application ‘sieveshell’.


%prep
%forgeautosetup -p1 -S git


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Generate man pages using Sphinx
pushd docs
make man
popd


%install
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a docs/_build/man/*.1 %{buildroot}/%{_mandir}/man1
cp %{buildroot}/%{_mandir}/man1/%{pypi_name}.1 %{buildroot}/%{_mandir}/man1/sieveshell.1

%pyproject_install
%pyproject_save_files managesieve


%check
%pytest


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.txt HISTORY
%{_mandir}/man1/%{pypi_name}.1*
%{_mandir}/man1/sieveshell.1*
%{_bindir}/sieveshell


%changelog
%autochangelog
