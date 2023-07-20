%global mmm_modules_dir %{nodejs_sitelib}/magicmirror/modules

%global srcname MMM-AirNow
%global srcversion 1.0.0
%global forgeurl https://github.com/nigel-daniels/%{srcname}
%global commit efddeb369d4bb454194e7ed5bb48d38f06c890a9
%global date 20200824

%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           magicmirror-module-airnow
Version:        %{srcversion}^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        MagicMirror² module to show air quality based on the US AirNow API

License:        Apache-2.0 and BSD and ISC and MIT and Unlicense
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
Source1:        %{srcname}-%{srcversion}-nm-prod.tgz
Source2:        %{srcname}-%{srcversion}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel
Requires:       magicmirror

%description
This is a module for the MagicMirror. This module shows air quality based on
the US AirNow API.

%prep
%setup -q -n %{srcname}-%{commit}
cp %{SOURCE2} .

%build
# Setup bundled node modules
tar xfz %{SOURCE1}
# Delete this to prevent an unnecessary dependency on
# /usr/bin/./node_modules/.bin/coffee
rm -r node_modules_prod/performance-now/test/
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%install
mkdir -p %{buildroot}%{mmm_modules_dir}/%{srcname}
cp -pr package.json airnow.css airquality.png *.js \
  %{buildroot}%{mmm_modules_dir}/%{srcname}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{mmm_modules_dir}/%{srcname}

%check
%nodejs_symlink_deps --check

%files
%doc README.md
%license LICENSE %{srcname}-%{srcversion}-bundled-licenses.txt
%{mmm_modules_dir}/%{srcname}

%changelog
%autochangelog
