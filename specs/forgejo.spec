%bcond check 1

# Set --with bundle_vendored to bundle vendored sources into tarballs
%bcond bundle_vendored 0
# Set --with bundle_vendored_force to overwrite existing archive files
%bcond bundle_vendored_force 0

%global goipath forgejo.org
%global forgeurl https://codeberg.org/forgejo/forgejo

%global _local_file_attrs node_deps
%global __node_deps_provides %{S:10} %{_builddir}/%{name}-src-%{version}/package-lock.json
%global __node_deps_path ^%{_bindir}/%{name}$

Name:           forgejo
Version:        13.0.4
Release:        %autorelease
Summary:        A lightweight software forge

# CC0-1.0 is normally not permissible for code in Fedora. Because the vendored Go package
# github.com/zeebo/blake3 it applies to has been available in Fedora as golang-github-zeebo-blake3
# since before the cutoff date 2022-08-01, the exception to use it also applies here.
%global vendored_go_mod_licenses 0BSD AND AGPL-3.0-only AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later AND ICU AND ISC AND MIT AND MPL-2.0 AND (FTL OR GPL-2.0-or-later)

# Determined using forgejo-node-get-licenses.py
%global vendored_node_mod_licenses Apache-2.0 AND LGPL-3.0-or-later AND Unlicense AND PSF-2.0 AND (BSD-2-Clause OR MIT OR Apache-2.0) AND CC-BY-4.0 AND CC-BY-3.0 AND MIT-0 AND Apache-2.0 AND LGPL-3.0-only AND BSD-2-Clause AND LGPL-3.0-or-later AND (MIT OR Apache-2.0) AND Apache-2.0 AND LGPL-3.0-or-later AND MIT AND ISC AND BSD-3-Clause AND BlueOak-1.0.0 AND (MPL-2.0 OR Apache-2.0) AND MPL-2.0 AND 0BSD AND CC0-1.0 AND MIT AND (MIT AND CC-BY-3.0) AND (MIT OR CC0-1.0)

# Forgejo itself is "MIT AND GPL-3.0-or-later", the following is the combination with vendored
# sources.
License:        MIT AND GPL-3.0-or-later AND (%vendored_go_mod_licenses) AND (%vendored_node_mod_licenses)
URL:            https://forgejo.org
%global         src_tarball %{forgeurl}/releases/download/v%{version}/%{name}-src-%{version}.tar.gz
# The official tarball contains pre-generated, minified JS files. Previously, we used an
# automatically generated tarball and regenerated everything (bundled Go and Node modules) which
# proved to be pretty fragile, e.g. when updates pulled in new tools from the NodeJS universe which
# were shipped as pre-built native executables for a number of platforms. This was worked around but
# it took a lot of effort. To resolve this issue, we decided in the team working on Fedora Forgejo
# deployment to revert to using the official tarball. Additionally, it gives us back verifying
# the integrity of the tarball with the upstream GnuPG key.
Source0:        %{src_tarball}
Source1:        %{src_tarball}.asc
Source2:        https://openpgpkey.forgejo.org/.well-known/openpgpkey/forgejo.org/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/dj3498u4hyyarh35rkjfnghbjxug6b19.pgp

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

ExclusiveArch:  %golang_arches_future

BuildRequires:  coreutils
BuildRequires:  gnupg2
BuildRequires:  go-rpm-macros
BuildRequires:  golang-bin >= 1.23
BuildRequires:  golang-src >= 1.23
BuildRequires:  go-vendor-tools
BuildRequires:  make
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
%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%autosetup -N -n %{name}-src-%{version}
patch --input=%{PATCH0} --output=app.ini.tmpl custom/conf/app.example.ini


%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:3}


%build
# Build manually rather than using the Makefile, so globally defined flags are applied.
%global gomodulesmode GO111MODULE=on
%global gotags bindata timetzdata sqlite sqlite_unlock_notify
%global gobuildflags %{?gobuildflags} -tags '%gotags'

go generate -tags '%gotags' ./...

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
