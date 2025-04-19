%global pkgname pnpm

Name:           nodejs-%{pkgname}
Version:        10.8.1
Release:        %{autorelease}
Summary:        Fast, disk space efficient package manager

# MIT is the pnpm license the others are from modules
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND ISC
URL:            https://pnpm.io
Source0:        http://registry.npmjs.org/%{pkgname}/-/%{pkgname}-%{version}.tgz
Source3:        %{pkgname}-%{version}-bundled-licenses.txt

BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  typescript
Requires:       bash
Provides:       npm(%{pkgname}) = %{version}

%global _description %{expand:
A fast, disk space efficient package manager for NodeJS.
}

%description %{_description}


%package -n %{pkgname}
Summary:        Fast, disk space efficient package manager

%description -n %{pkgname} %{_description}


%prep
%autosetup -p1 -n package
cp %{SOURCE3} .


%build
# nothing to do

%install
CFLAGS="%{optflags}"
export CFLAGS
CXXFLAGS="%{optflags}"
export CXXFLAGS

npm_config_prefix=%{buildroot}%{_prefix}
export npm_config_prefix

install -d %{buildroot}%{nodejs_sitearch}

npm install -g %{SOURCE0}

# HACK: Move pnpm to the right location.
# I haven't found a npm config for `<prefix>/lib/node_modules` yet.
mv %{buildroot}$(dirname %{nodejs_sitearch})/node_modules/%{pkgname} %{buildroot}%{nodejs_sitearch}
# Fix symlinks
ln -sf ..//lib/$(basename %{nodejs_sitearch})/%{pkgname}/bin/pnpm.cjs %{buildroot}%{_bindir}/pnpm
ln -sf ../lib/$(basename %{nodejs_sitearch})/%{pkgname}/bin/pnpx.cjs %{buildroot}%{_bindir}/pnpx

# Fix shebang in pnp(m|x)
sed -i -e 's|#!%{_bindir}/env node|#!%{_bindir}/node|' %{buildroot}%{nodejs_sitelib}/%{pkgname}/bin/*

### CLEANUP
# Remove hidden files
find %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules -type f -name '.*' -delete

# Remove hidden directories
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/.pnpm
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/balanced-match/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/cacache/node_modules/brace-expansion/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/iconv-lite/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/iconv-lite/.idea

# Removed unused modules
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/node-gyp
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}/dist/node_modules/node-gyp-bin

# Remove duplicates
%fdupes %{buildroot}%{nodejs_sitelib}/%{pkgname}


%check
# This prints the help by default
%{__nodejs} -e 'require("./")' | grep "^Version %{version}"


%files -n %{pkgname}
%license LICENSE %{pkgname}-%{version}-bundled-licenses.txt
%doc README.md
%{_bindir}/pnpm
%{_bindir}/pnpx
%{nodejs_sitearch}/pnpm

%changelog
%{autochangelog}
