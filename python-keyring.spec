%bcond tests 1
# The xvfb tests sometimes hang in koji.
%bcond xvfb_tests 0

Name:           python-keyring
Version:        24.3.1
Release:        %autorelease
Summary:        Store and access your passwords safely

# SPDX
License:        MIT
URL:            https://github.com/jaraco/keyring
Source:         %{pypi_source keyring}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  help2man

%if %{with tests}
# The “testing” extra mostly brings in linters and similar, which we would have
# to patch out. Instead, we BR pytest manually. See:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  python3dist(pytest)
%if %{with xvfb_tests}
# Run graphical tests in non-graphical build environment.
BuildRequires:  xorg-x11-server-Xvfb
# Enable libsecret backend
BuildRequires:  python3-gobject
BuildRequires:  libsecret
BuildRequires:  gnome-keyring
BuildRequires:  /usr/bin/dbus-launch
%endif
%endif

%global desc %{expand:
The Python keyring library provides an easy way to access the system keyring
service from python. It can be used in any application that needs safe password
storage.

These recommended keyring backends are supported:

  • macOS Keychain
  • Freedesktop Secret Service supports many DE including GNOME (requires
    secretstorage)
  • KDE4 & KDE5 KWallet (requires dbus)
  • Windows Credential Locker

Other keyring implementations are available through third-party backends.}


%description %desc


%package -n     python3-keyring
Summary:        Python 3 library to access the system keyring service

Recommends:     python3-keyring+completion = %{version}-%{release}

%description -n python3-keyring %desc


# We don’t use “%%pyproject_extras_subpkg -n python3-keyring completion”
# because we want to add the completion scripts to the files list and provide a
# custom summary and description.
%package -n     python3-keyring+completion
Summary:        Shell completion support for the keyring command

Requires:       python3-keyring = %{version}-%{release}

%description -n python3-keyring+completion
This package:

• Makes sure the “completion” extra dependencies are installed
• Installs the actual shell completion scripts

There may be additional requirements to enable completion support *in general*
for a particular shell. For example, bash needs the bash-completion package to
be installed.


%prep
%setup -q -n keyring-%{version}

# This will be installed in site-packages without the executable bit set, so
# the shebang should be removed.
sed -r -i '1{/^#!/d}' keyring/cli.py


%generate_buildrequires
%pyproject_buildrequires -x completion


%build
%pyproject_wheel

for sh in bash zsh tcsh
do
  PYTHONPATH="${PWD}/build/lib" '%{python3}' -m keyring \
      --print-completion "${sh}" | tee "keyring.${sh}"
done


%install
%pyproject_install
%pyproject_save_files -l keyring
install -D -p -m 0644 keyring.bash \
    '%{buildroot}%{bash_completions_dir}/keyring'
install -D -p -m 0644 keyring.zsh \
    '%{buildroot}%{zsh_completions_dir}/_keyring'
install -D -p -m 0644 keyring.tcsh \
    '%{buildroot}%{_sysconfdir}/profile.d/keyring.csh'

# Do this in %%install rather than in %%build so we can use the actual
# generated entry point
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man \
    --no-info \
    --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/keyring.1' \
    '%{buildroot}%{_bindir}/keyring'


%check
%if %{with tests}
%if %{with xvfb_tests}
%global __pytest /usr/bin/xvfb-run -a /usr/bin/pytest
%endif
%pytest
%endif


%files -n python3-keyring -f %{pyproject_files}
%doc NEWS.rst
%doc README.rst

%{_bindir}/keyring
%{_mandir}/man1/keyring.1*


%files -n python3-keyring+completion
%{bash_completions_dir}/keyring
%{zsh_completions_dir}/_keyring
%config(noreplace) %{_sysconfdir}/profile.d/keyring.csh

%ghost %{python3_sitelib}/*.dist-info


%changelog
%autochangelog
