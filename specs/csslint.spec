%global npm_name csslint
%global forgeurl https://github.com/CSSLint/csslint
Version:        1.0.5

%forgemeta

Name:           %{npm_name}
Release:        %autorelease
Summary:        Detecting potential problems in CSS code

License:        MIT
URL:            http://csslint.net/
Source0:        %{forgesource}
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       nodejs >= 0.10.0
BuildRequires:  nodejs-devel


%description
CSSLint is a tool to help point out problems with your CSS code. It does basic
syntax checking as well as applying a set of rules to the code that look for
problematic patterns or signs of inefficiency. The rules are all pluggable, so
you can easily write your own or omit ones you don't want.


%prep
%forgesetup

cp %{SOURCE3} .
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd


%build
chmod a+x dist/cli.js


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}/
cp -pr package.json dist/* %{buildroot}%{nodejs_sitelib}/%{npm_name}/
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{npm_name}/

mkdir -p %{buildroot}%{_bindir}/
ln -sf %{nodejs_sitelib}/%{npm_name}/cli.js %{buildroot}%{_bindir}/%{name}


%check
%{__nodejs} -e 'require("./")'
tar xfz %{SOURCE2}
pushd node_modules
ln -s ../node_modules_dev/* .
popd
node_modules_dev/.bin/grunt test


%files
%doc CHANGELOG README.md
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%{_bindir}/%{name}
%{nodejs_sitelib}/%{npm_name}


%changelog
%autochangelog
