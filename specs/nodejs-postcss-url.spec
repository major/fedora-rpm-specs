%global npm_name postcss-url
%define _description PostCSS plugin to rebase, inline or copy on url()


Name:           nodejs-%{npm_name}
Version:        10.1.3
Release:        %autorelease
Summary:        %{_description}

# The source code is licensed under the MIT, and the bundled node_modules contains ISC
# and MIT licenses.
License:        ISC AND MIT
URL:            https://github.com/postcss/%{npm_name}
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel

Requires:       nodejs


%description
%{_description}.


%prep
%autosetup -n package
cp %{SOURCE3} .
# Setup bundled runtime(prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd


%build
# nothing to build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr src %{buildroot}%{nodejs_sitelib}/%{npm_name}
# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{npm_name}


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'


%files
# The LICENSE file is from the source code, the licenses from bundled node_modules
# are in the bundled licenses file.
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%doc README.md
%{nodejs_sitelib}/%{npm_name}


%changelog
%autochangelog
