%bcond check 1

%global goipath forgejo.org
%global forgeurl https://codeberg.org/forgejo/forgejo
%global gosource %{forgeurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%global _local_file_attrs node_deps
%global __node_deps_provides %{S:10} %{_builddir}/%{name}-src-%{version}/package-lock.json
%global __node_deps_path ^%{_bindir}/%{name}$

%global pagure_migrator_gitrev c9a5694dd2

Name:           forgejo
Version:        11.0.3
Release:        %autorelease
Summary:        A lightweight software forge

# CC0-1.0 is normally not permissible for code in Fedora. Because the vendored Go package
# github.com/zeebo/blake3 it applies to has been available in Fedora as golang-github-zeebo-blake3
# since before the cutoff date 2022-08-01, the exception to use it also applies here.
%global vendored_go_mod_licenses Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-or-later AND ICU AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT AND MPL-2.0 AND (FTL OR GPL-2.0-or-later)

# Determined using forgejo-node-get-licenses.py
%global vendored_node_mod_licenses (BSD-2-Clause OR MIT OR Apache-2.0) AND BSD-3-Clause AND ISC AND PSF-2.0 AND CC-BY-3.0 AND Apache-2.0 AND (MIT OR CC0-1.0) AND MIT AND (MIT OR Apache-2.0) AND BlueOak-1.0.0 AND MIT-0 AND (MIT AND CC-BY-3.0) AND 0BSD AND MPL-2.0 AND BSD-2-Clause AND LGPL-3.0-only AND CC0-1.0 AND CC-BY-4.0 AND (MPL-2.0 OR Apache-2.0) AND Unlicense

# Forgejo itself is "MIT AND GPL-3.0-or-later", the following is the combination with vendored
# sources.
License:        MIT AND GPL-3.0-or-later AND %vendored_go_mod_licenses AND %vendored_node_mod_licenses
URL:            https://forgejo.org
Source0:        %{gosource}
# Generated by go-vendor-tools after `fedpkg prep`:
# go_vendor_archive create \
#     --top-level-dir -O forgejo-%%{version}-go-vendor.tar.bz2 \
#     --config=go-vendor-tools.toml \
#     forgejo-%%{version}-build/forgejo
Source1:        %{name}-%{version}-go-vendor.tar.bz2
# Generated after `fedpkg prep`:
# (
#     cd forgejo-%%{version}-build/forgejo
#     rm -rf node_modules/
#     npm uninstall esbuild-loader
#     npm install --omit=optional --no-save
#     rm -r node_modules/*esbuild*
#     cd ..
#     tar -cvaf ../%%{name}-%%{version}-nodejs-vendor.tar.xz forgejo/node_modules
# )
Source2:        %{name}-%{version}-nodejs-vendor.tar.xz
Source3:        go-vendor-tools.toml
Source4:        robots.txt
Source5:        forgejo.service
Source6:        forgejo-init.service
Source7:        forgejo-init.sh
Source8:        forgejo.sysusers.conf
Source9:        forgejo.sysconfig
Source10:       forgejo-node-deps-provides.py
Source11:       forgejo-node-get-licenses.py

Patch0:         forgejo-10.0.1-app.ini.tmpl.patch
Patch1:         forgejo-11.0.2-no-esbuild-loader.patch
Patch2:         forgejo-11.0.1-webpack-mock-crash.patch
# Pagure migrator plugin. Generate from the pagure-migrator branch of
# https://codeberg.org/ryanlerch/forgejo like this (assuming the branch is based off of the
# v12.0/forge upstream branch):
# git diff $(git merge-base v12.0/forgejo pagure-migrator) pagure-migrator | \
#     gzip -9 -c > %%{name}-pagure-migrator-%%{pagure_migrator_gitrev}.patch.gz
Patch3:         %{name}-pagure-migrator-%{pagure_migrator_gitrev}.patch.gz


# Remove shebang from bash autocompletion snippet
# https://codeberg.org/forgejo/forgejo/pulls/8137
Patch10:        https://codeberg.org/forgejo/forgejo/pulls/8137.patch

ExclusiveArch:  %golang_arches_future

BuildRequires:  coreutils
BuildRequires:  go-rpm-macros
BuildRequires:  golang-bin >= 1.23
BuildRequires:  golang-src >= 1.23
BuildRequires:  go-vendor-tools
BuildRequires:  make
BuildRequires:  nodejs-npm
BuildRequires:  python3
# For forgejo-node-get-licenses.py
# BuildRequires:  python3dist(license-expression)
BuildRequires:  sed
BuildRequires:  sqlite-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  util-linux-core

Requires:       bash
Requires:       coreutils
Requires:       git-core
Requires:       git-lfs
Requires:       sed
%{?sysusers_requires_compat}

%description
Forgejo (pronounced /forˈd͡ʒe.jo/) is a lightweight software forge. Use it to
host git repositories, track their issues and allow people to contribute to
them!

%prep
%autosetup -N -n %{name}
patch --input=%{PATCH0} --output=app.ini.tmpl custom/conf/app.example.ini
%patch 1 -p1 -b .no-esbuild-loader
%patch 2 -p1 -b .webpack-mock-patch
%patch 3 -p1 -b .pagure-migrator
%patch 10 -p1 -b .bash-completion

tar --strip-components=1 -xf %{S:1}
tar --strip-components=1 -xf %{S:2}


%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:3}


%build
# Step through "make build", but do some steps manually rather than using the Makefile, so globally
# defined flags are applied.
%global gomodulesmode GO111MODULE=on
%global gotags bindata timetzdata sqlite sqlite_unlock_notify
%global gobuildflags %{?gobuildflags} -tags '%gotags'

# make webpack
BROWSERSLIST_IGNORE_OLD_DATA=true npx webpack

make %{?_smp_mflags} TAGS="%gotags" generate-go

export GO_LDFLAGS=" \
    -X \"forgejo.org/modules/setting.CustomPath=%{_sysconfdir}/%{name}\" \
    -X \"forgejo.org/modules/setting.CustomConf=%{_sysconfdir}/%{name}/conf/app.ini\" \
    -X \"forgejo.org/modules/setting.AppWorkPath=%{_sharedstatedir}/%{name}\" \
    -X \"main.Tags=%{gotags}\" \
    -X \"main.ReleaseVersion=%{version}-%{release}\" \
    -X \"main.Version=%{version}-%{release}\" \
"
%gobuild -o forgejo %{goipath}

sed -e 's/gitea/%{name}/g' \
    < contrib/autocompletion/bash_autocomplete \
    > %{name}.complete
touch -r contrib/autocompletion/bash_autocomplete %{name}.complete

%install
%go_vendor_license_install -c %{S:3}
install -m755 -d %{buildroot}%{_defaultlicensedir}/%{name}/public/assets
install -m644 public/assets/licenses.txt %{buildroot}%{_defaultlicensedir}/%{name}/public/assets/
install -m755 -d %%{buildroot}{_defaultlicensedir}/%{name}/vendor
install -m644 vendor/modules.txt %{buildroot}%{_defaultlicensedir}/%{name}/vendor/

install -m755 -D %{name} %{buildroot}%{_bindir}/%{name}

install -m755 -d \
    %{buildroot}%{_sysconfdir}/%{name}/conf \
    %{buildroot}%{_sysconfdir}/%{name}/public/assets \
    %{buildroot}%{_sysconfdir}/%{name}/templates

install -m644 -p -D app.ini.tmpl %{buildroot}%{_sysconfdir}/%{name}/conf/app.ini.tmpl
install -m644 -p -D %{S:4} %{buildroot}%{_sysconfdir}/%{name}/public/robots.txt
install -m644 -p -D %{name}.complete %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -m644 -p -D %{S:5} %{buildroot}%{_unitdir}/%{name}.service
install -m644 -p -D %{S:6} %{buildroot}%{_unitdir}/%{name}-init.service
install -m755 -p -D %{S:7} %{buildroot}%{_libexecdir}/%{name}-init
install -m644 -p -D %{S:8} %{buildroot}%{_sysusersdir}/%{name}.conf

install -m750 -d \
    %{buildroot}%{_sharedstatedir}/%{name} \
    %{buildroot}%{_sharedstatedir}/%{name}/data \
    %{buildroot}%{_sharedstatedir}/%{name}/log

install -m640 -D %{S:9} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

# We carry so many copies of the same license files…
hardlink --ignore-time %{buildroot}


%check
%go_vendor_license_check -c %{S:3} %{vendored_go_mod_licenses}


%pre
%sysusers_create_compat %{S:8}


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%files -f %{go_vendor_license_filelist}
%dir %license %{_defaultlicensedir}/%{name}/public
%dir %license %{_defaultlicensedir}/%{name}/public/assets
%license %{_defaultlicensedir}/%{name}/public/assets/licenses.txt
%license %{_defaultlicensedir}/%{name}/vendor/modules.txt
%doc CONTRIBUTING.md README.md RELEASE-NOTES.md
%doc custom/conf/app.example.ini

%{_bindir}/%{name}

%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf
%dir %{_sysconfdir}/%{name}/public
%dir %{_sysconfdir}/%{name}/public/assets
%dir %{_sysconfdir}/%{name}/templates
%{_sysconfdir}/%{name}/conf/app.ini.tmpl
%attr(0640,-,%{name}) %ghost %config(noreplace,missingok) %{_sysconfdir}/%{name}/conf/app.ini
%config(noreplace) %{_sysconfdir}/%{name}/public/robots.txt
%config(noreplace,missingok) %{_sysconfdir}/sysconfig/%{name}

%{_sysusersdir}/%{name}.conf
%{_datadir}/bash-completion/completions/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-init.service
%{_libexecdir}/%{name}-init

%attr(0750,%{name},%{name}) %dir %{_sharedstatedir}/%{name}
%attr(0750,%{name},%{name}) %dir %{_sharedstatedir}/%{name}/data
%attr(0750,%{name},%{name}) %dir %{_sharedstatedir}/%{name}/log

%changelog
%autochangelog
