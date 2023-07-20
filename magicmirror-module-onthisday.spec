%global mmm_modules_dir %{nodejs_sitelib}/magicmirror/modules

%global srcname MMM-OnThisDay
%global srcversion 0.1.1
%global forgeurl https://github.com/nkl-kst/%{srcname}
%global commit 459fd61f3b5e56a19c898116de203a1a081b356b
%global date 20220120

%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           magicmirror-module-onthisday
Version:        %{srcversion}^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Display historical events on your MagicMirror

License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
Source1:        %{srcname}-%{srcversion}-nm-prod.tgz
Source2:        %{srcname}-%{srcversion}-nm-dev.tgz
Source3:        %{srcname}-%{srcversion}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel
Requires:       magicmirror

%description
This is a module for MagicMirror². It displays historical events from Wikipedia
based on the current date.

%prep
%setup -q -n %{srcname}-%{commit}
cp %{SOURCE3} .

%build
# Setup bundled node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%install
mkdir -p %{buildroot}%{mmm_modules_dir}/%{srcname}
cp -pr package.json %{srcname}.css %{srcname}.njk *.js translation \
  %{buildroot}%{mmm_modules_dir}/%{srcname}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{mmm_modules_dir}/%{srcname}

%check
%nodejs_symlink_deps --check
# Setup bundled dev node_modules for testing
tar xfz %{SOURCE2}
pushd node_modules
ln -sf ../node_modules_dev/* .
popd
pushd node_modules/.bin
ln -sf ../../node_modules_dev/.bin/* .
popd
# Run tests
./node_modules/.bin/mocha test/unit --recursive
# The functional tests require Internet access
# ./node_modules/.bin/mocha test/functional --recursive

%files
%doc CHANGELOG.md README.md screenshot
%license LICENSE.txt %{srcname}-%{srcversion}-bundled-licenses.txt
%{mmm_modules_dir}/%{srcname}

%changelog
%autochangelog
