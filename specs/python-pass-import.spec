%global srcname pass-import
# as of 2024-12-31 only f42 has jsonpath_ng 1.7.0
# pass_import.__main__.py imports from exceptions.py
# which is not available on jsonpath_ng 1.5.0
%if %{exists:%{python3_sitelib}/jsonpath_ng/exceptions.py}
%global has_jsonpath_ng_170 0
%endif

Name:          python-%{srcname}
Version:       3.5
Release:       %autorelease
Summary:       A pass extension for importing data from most existing password managers
License:       GPL-3.0-or-later

URL:           https://github.com/roddhjav/pass-import
Source0:       %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
Source1:       %{url}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz.asc
Source2:       https://pujol.io/keys/0xc5469996f0df68ec.asc
Patch:         0001-Fix-shebangs.patch

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pytest)
BuildRequires: gnupg2
BuildRequires: pass

Requires:      pass

%global _description %{expand:
pass import is a password store extension allowing you to import your password
database to a password store repository conveniently. It natively supports
import from 62 different password managers. More manager support can easily be
added.}

%description %{_description}

%package -n python3-%{srcname}
Summary:    %{summary}

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} xml keepass gnomekeyring encrypted_otp decrypt %{?has_jsonpath_ng_170:filter}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x all

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pass_import
# setup.py through data_files puts files that should be in /usr/share and /usr/lib
# under site-packages, so move them out of there
mv %{buildroot}{%{python3_sitelib}%{_datadir},%{_prefix}}
mv %{buildroot}{%{python3_sitelib}%{_prefix}/lib/password-store,%{_prefix}/lib}

# no completion for "pass import" when not doing that move
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
mv %{buildroot}%{bash_completions_dir}/%{srcname} %{buildroot}%{_sysconfdir}/bash_completion.d/%{srcname}

%check
# 1) test_open_networkmanager requires network, so it is naturally disabled
# 2) test_import_gnome_keyring requires working gnome-keyring
#    there is a file in tests/assets/db/gnome-keyring.keyring but it isn't
#    imported automatically. Importing it manually crashes gnome-keyring
%pytest -k "not test_open_networkmanager and \
            %{!?has_jsonpath_ng_170:not test_filter_on_non_empty_data_source and} \
            not test_import_gnome_keyring"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_mandir}/man1/pimport.1*
%{_mandir}/man1/pass-import.1*
%{_bindir}/pimport
%{_prefix}/lib/password-store/extensions/import.bash
%{_sysconfdir}/bash_completion.d/%{srcname}
%{bash_completions_dir}/pimport
%{zsh_completions_dir}/_%{srcname}
%{zsh_completions_dir}/_pimport

%changelog
%autochangelog
