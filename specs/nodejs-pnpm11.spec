%global pkgname pnpm
%global pnpm_major_version 11

Name:           nodejs-%{pkgname}%{pnpm_major_version}
Version:        11.27.0
Release:        %autorelease
Summary:        Fast, disk space efficient package manager

# MIT is the pnpm license the others are from modules
License:        MIT AND Apache-2.0 AND BlueOak-1.0.0 AND ISC
URL:            https://pnpm.io
Source0:        https://registry.npmjs.org/%{pkgname}/-/%{pkgname}-%{version}.tgz
Source3:        %{pkgname}-%{version}-bundled-licenses.txt

BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-npm

%global _description %{expand:
A fast, disk space efficient package manager for NodeJS.
}

%description %{_description}


%package -n %{pkgname}%{pnpm_major_version}
Summary:        Fast, disk space efficient package manager
Requires:       bash
Provides:       npm(%{pkgname}) = %{version}
Requires(post): %{_bindir}/update-alternatives
Requires(postun): %{_bindir}/update-alternatives

# The old unversioned "pnpm" package owns /usr/bin/pnpm and /usr/bin/pnpx as
# real files, not via alternatives. Conflict on its package.
Conflicts:      pnpm

%description -n %{pkgname}%{pnpm_major_version} %{_description}


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

npm install -g  --offline --no-audit --no-fund %{SOURCE0}

# Move to a versioned module directory so pnpm10/pnpm11/pnpm12 etc. can coexist
mv %{buildroot}%{nodejs_sitelib}/%{pkgname} %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}

# Drop the unversioned bin symlinks npm just created, we ship versioned ones instead
rm -f %{buildroot}%{_bindir}/{pnpm,pnpx,pn,pnx}

# Fix symlinks
ln -sf ../lib/$(basename %{nodejs_sitearch})/%{pkgname}%{pnpm_major_version}/bin/pnpm.mjs %{buildroot}%{_bindir}/pnpm%{pnpm_major_version}
ln -sf ../lib/$(basename %{nodejs_sitearch})/%{pkgname}%{pnpm_major_version}/bin/pnpx.mjs %{buildroot}%{_bindir}/pnpx%{pnpm_major_version}
ln -sf ../lib/$(basename %{nodejs_sitearch})/%{pkgname}%{pnpm_major_version}/bin/pnpm.mjs %{buildroot}%{_bindir}/pn%{pnpm_major_version}
ln -sf ../lib/$(basename %{nodejs_sitearch})/%{pkgname}%{pnpm_major_version}/bin/pnpx.mjs %{buildroot}%{_bindir}/pnx%{pnpm_major_version}

# Fix shebang in pnp(m|x)
sed -i -e 's|#!%{_bindir}/env node|#!%{_bindir}/node|' %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/bin/*

### CLEANUP
# Remove hidden files
find %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules -type f -name '.*' -delete

# Remove hidden directories
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules/.pnpm
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules/balanced-match/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules/cacache/node_modules/brace-expansion/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules/iconv-lite/.github
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules/iconv-lite/.idea

# Removed unused modules
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules/node-gyp
rm -rf %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}/dist/node_modules/node-gyp-bin

# Remove duplicates
%fdupes %{buildroot}%{nodejs_sitelib}/%{pkgname}%{pnpm_major_version}


%check
# This prints the help by default
%{__nodejs} -e 'require("./bin/pnpm.cjs")' | grep "^Version %{version}"
%{__nodejs} bin/pnpm.mjs | grep "^Version %{version}"


%post -n %{pkgname}%{pnpm_major_version}
%{_sbindir}/update-alternatives --install %{_bindir}/pnpm pnpm %{_bindir}/pnpm%{pnpm_major_version} %{pnpm_major_version} \
    --slave %{_bindir}/pnpx pnpx %{_bindir}/pnpx%{pnpm_major_version} \
    --slave %{_bindir}/pn pn %{_bindir}/pn%{pnpm_major_version} \
    --slave %{_bindir}/pnx pnx %{_bindir}/pnx%{pnpm_major_version}


%postun -n %{pkgname}%{pnpm_major_version}
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove pnpm %{_bindir}/pnpm%{pnpm_major_version}
fi


%files -n %{pkgname}%{pnpm_major_version}
%license LICENSE %{pkgname}-%{version}-bundled-licenses.txt
%license  %{nodejs_sitearch}/%{pkgname}%{pnpm_major_version}/dist/node_modules/env-paths/license
%doc README.md
%{_bindir}/pnpm%{pnpm_major_version}
%{_bindir}/pnpx%{pnpm_major_version}
%{_bindir}/pn%{pnpm_major_version}
%{_bindir}/pnx%{pnpm_major_version}
%ghost %{_bindir}/pnpm
%ghost %{_bindir}/pnpx
%ghost %{_bindir}/pn
%ghost %{_bindir}/pnx
%exclude %{nodejs_sitearch}/%{pkgname}%{pnpm_major_version}/dist/node_modules/env-paths/license
%{nodejs_sitearch}/%{pkgname}%{pnpm_major_version}

%changelog
%autochangelog
