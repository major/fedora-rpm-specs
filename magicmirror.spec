%bcond_without tests
%global srcname MagicMirror
%global forgeurl https://github.com/MagicMirrorOrg/MagicMirror

Name:           magicmirror
Version:        2.26.0
Release:        %autorelease
Summary:        Modular smart mirror platform

# MagicMirror itself is MIT, the rest comes from the dependencies
License:        0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND (CC-BY-4.0 AND OFL-1.1 AND MIT) AND ISC AND MIT AND OFL-1.1 AND Python-2.0
URL:            http://magicmirror.builders
# Use the GitHub tarball due to https://github.com/MichMich/MagicMirror/issues/2876
Source0:        %{forgeurl}/archive/v%{version}/%{srcname}-%{version}.tar.gz
# Created with nodejs-packaging >= 2021.06-7 running:
#   nodejs-packaging-bundler MagicMirror 2.26.0 MagicMirror-2.26.0.tar.gz
Source1:        %{srcname}-%{version}-nm-prod.tgz
Source2:        %{srcname}-%{version}-nm-dev.tgz
Source3:        %{srcname}-%{version}-bundled-licenses.txt
Source4:        %{name}.service
Source5:        %{name}.sysusers

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       nodejs
BuildRequires:  nodejs-devel
BuildRequires:  systemd-rpm-macros

%if %{with tests}
# For tests/e2e/serveronly_spec.js
%if 0%{?fedora} || 0%{?rhel} > 9
BuildRequires:  nodejs-npm
%else
BuildRequires:  npm
%endif
%endif

# Remove once f39 and epel9 are EOL
Provides:       magicmirror-rpm-macros = %{version}-%{release}
Obsoletes:      magicmirror-rpm-macros < 2.22.0-2

%description
MagicMirror² is an open source modular smart mirror platform. With a growing
list of installable modules, the MagicMirror² allows you to convert your
hallway or bathroom mirror into your personal assistant.

This package contains the server version of MagicMirror², which is meant to be
accessed via a browser.

%prep
%setup -q -n %{srcname}-%{version}
cp %{SOURCE3} .

%build
# Setup bundled node modules
tar xfz %{SOURCE1}
for dir in node_modules fonts/node_modules vendor/node_modules; do
  mkdir -p "$dir"
  pushd "$dir"
  ln -s ../node_modules_prod/* .
  [ -e ../node_modules_prod/.bin ] && ln -s ../node_modules_prod/.bin .
  popd
done

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json fonts/ index.html js/ modules/ serveronly/ translations/ vendor/ \
  %{buildroot}%{nodejs_sitelib}/%{name}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{name}

# Install config files
install -Dpm0644 config/config.js.sample %{buildroot}%{_sysconfdir}/%{name}/config.js
install -Dpm0644 css/custom.css.sample %{buildroot}%{_sysconfdir}/%{name}/custom.css
install -Ddpm0755 %{buildroot}%{nodejs_sitelib}/%{name}/config
ln -s %{_sysconfdir}/%{name}/config.js %{buildroot}%{nodejs_sitelib}/%{name}/config
install -Dpm0644 -t %{buildroot}%{nodejs_sitelib}/%{name}/css css/main.css
ln -s %{_sysconfdir}/%{name}/custom.css %{buildroot}%{nodejs_sitelib}/%{name}/css

# Install systemd unit
install -Dpm0644 -t %{buildroot}%{_unitdir} %{SOURCE4}
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/%{name}.conf

%if %{with tests}
%check
%nodejs_symlink_deps --check
# Setup bundled dev node_modules for testing
tar xfz %{SOURCE2}
for dir in node_modules fonts/node_modules vendor/node_modules; do
  pushd "$dir"
  ln -sf ../node_modules_dev/* .
  popd
  if [ -e "${dir}/.bin" ]; then
    pushd "${dir}/.bin"
    [ -e ../../node_modules_dev/.bin ] && ln -sf ../../node_modules_dev/.bin/* .
    popd
  fi
done
# Required for the e2e tests
ln -s custom.css.sample css/custom.css
# Run tests
./node_modules/.bin/jest \
  --modulePathIgnorePatterns node_modules_prod node_modules_dev \
  --selectProjects e2e unit \
  -i \
  --forceExit
%endif

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc CHANGELOG.md README.md
%license LICENSE.md %{srcname}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.js
%config(noreplace) %{_sysconfdir}/%{name}/custom.css
%{_sysusersdir}/%{name}.conf
%{_unitdir}/%{name}.service

%changelog
%autochangelog
