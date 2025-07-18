Name:           postcss-cli
Version:        11.0.1
Release:        %autorelease
Summary:         CLI for postcss, which transforms CSS styles with JS plugins

License:        Apache-2.0 AND BSD-3-Clause AND ISC AND MIT
URL:            https://postcss.org
Source0:        https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz
Source1:        %{name}-%{version}-nm-prod.tgz
Source2:        %{name}-%{version}-nm-dev.tgz
Source3:        %{name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

Requires:       nodejs
BuildRequires:  nodejs-devel

%description
PostCSS CLI is a command line interface for PostCSS, a tool for transforming
styles with JS plugins. These plugins can lint your CSS, support variables and
mixins, transpile future CSS syntax, inline images, and more.

%prep
%setup -q -n package
cp %{SOURCE3} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

%build
# nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json index.js lib/ %{buildroot}%{nodejs_sitelib}/%{name}/
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{name}/

mkdir -p %{buildroot}%{_bindir}
ln -s ../../%{nodejs_sitelib}/%{name}/index.js %{buildroot}%{_bindir}/postcss

%check
%{buildroot}%{_bindir}/postcss --help

%files
%doc README.md
%license LICENSE %{name}-%{version}-bundled-licenses.txt
%{nodejs_sitelib}/%{name}/
%{_bindir}/postcss

%changelog
%autochangelog
