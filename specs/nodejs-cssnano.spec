%global npm_name cssnano
%global _description %{expand:
Cssnano is a modern, modular compression tool written on top of the PostCSS
ecosystem, which allows us to use a lot of powerful features in order to
compact CSS appropriately.
}


Name:           nodejs-%{npm_name}
Version:        7.0.7
Release:        %autorelease
Summary:        A modular minifier, built on top of the PostCSS ecosystem

# The entire source code is MIT, and the rest is bundled licenses from node_modules
License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CC-BY-4.0 AND ISC AND MIT
URL:            https://github.com/cssnano/%{npm_name}
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:        %{npm_name}-%{version}-nm-prod.tgz
Source2:        %{npm_name}-%{version}-nm-dev.tgz
Source3:        %{npm_name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-devel, /usr/bin/node

Requires:       nodejs


%description
%{_description}


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
# LICENSE-MIT is the license from source code, and the bundled licenses are from node_modules
%license LICENSE-MIT %{npm_name}-%{version}-bundled-licenses.txt
%doc README.md
%{nodejs_sitelib}/%{npm_name}


%changelog
%autochangelog
