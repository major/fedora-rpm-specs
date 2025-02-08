%ifnarch %{qt6_qtwebengine_arches}
# No useful debug package unless qt frontend is built (see %%package qt below)
%global debug_package %{nil}
%endif

Name:           pgadmin4
# NOTE: Also regenerate requires as indicated below when updating!
# Verify Patch4 on next update
Version:        9.0
Release:        1%{?dist}
Summary:        Administration tool for PostgreSQL

# i686, armv7hl: The webpack terser plugin aborts with JS heap memory exhaustion on these arches
# s390x: wasm aborts with RuntimeError: memory access out of bounds when attempting to build webfonts-loader
# ppc64le: wasm aborts with RuntimeError: float unrepresentable in integer range
ExcludeArch:    i686 armv7hl s390x ppc64le

# PostgreSQL ist the main license, rest the bundled JS code (see %%{name}-%%{version}-vendor-licenses.txt)
License:        PostgreSQL AND MIT AND ISC AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND 0BSD AND BlueOak-1.0.0 AND CC-BY-4.0 AND OFL-1.1 AND Unlicense AND Python-2.0.1 AND Apache-2.0 WITH LLVM-exception AND (WTFPL OR MIT) AND Zlib AND CC-BY-3.0
URL:            https://www.pgadmin.org/
Source0:        https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v%{version}/source/pgadmin4-%{version}.tar.gz

# ./prepare_vendor.sh
Source1:        %{name}-%{version}-vendor.tar.xz
Source2:        %{name}-%{version}-vendor-licenses.txt
Source3:        %{name}-%{version}-yarn.lock

# Unofficial qt runtime
Source4:        pgadmin4-qt.cpp
Source5:        org.postgresql.pgadmin4.metainfo.xml
Source6:        pgadmin4-qt.svg

# Apache/WSGI config
Source7:        pgadmin4.conf

# Patch requirements for Fedora compat
Patch0:         pgadmin4_requirements.patch
# Fix python-azure-mgmt-rdbms-10.2.0~b5+ compatibility
Patch1:         pgadmin4_azure-mgmt-rdbms.patch
# Drop requirement on unpackaged python-sphinxcontrib-youtube
Patch2:         pgadmin4_sphinx_youtube.patch
# Drop packageManager field from package.json to avoid yarn complaining about corepack
Patch3:         pgadmin4_corepack.patch
# Don't store commit hash when building bundle
Patch4:         pgadmin4_no-git.patch

# Patch for building bundled mozjpeg
%global mozjpeg_ver 4.1.1
Source8:        https://github.com/mozilla/mozjpeg/archive/v%{mozjpeg_ver}/mozjpeg-%{mozjpeg_ver}.tar.gz
Patch100:       mozjpeg.patch

# For docs
BuildRequires:  glibc-langpack-en
BuildRequires:  python3-devel
BuildRequires:  python3-keyring
BuildRequires:  python3-sphinx
BuildRequires:  python3-setuptools
BuildRequires:  yarnpkg

# For node dependencies
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  yasm
BuildRequires:  optipng

# cd pgadmin4-<ver>
# patch -p1 < pgadmin4_requirements.patch
# python3 /usr/lib/rpm/redhat/pyproject_buildrequires.py -N requirements.txt --output requires 2>/dev/null && cat requires | awk '{print "Requires: "$0}'
Requires: python3dist(flask) >= 3
Requires: (python3dist(flask-login) >= 0 with python3dist(flask-login) < 1)
Requires: (python3dist(flask-mail) >= 0 with python3dist(flask-mail) < 1)
Requires: (python3dist(flask-migrate) >= 4 with python3dist(flask-migrate) < 5)
Requires: python3dist(flask-sqlalchemy) >= 3
Requires: (python3dist(flask-wtf) >= 1.2 with python3dist(flask-wtf) < 1.3)
Requires: (python3dist(flask-compress) >= 1 with python3dist(flask-compress) < 2)
Requires: (python3dist(flask-paranoid) >= 0 with python3dist(flask-paranoid) < 1)
Requires: (python3dist(flask-babel) >= 4 with python3dist(flask-babel) < 4.1)
Requires: python3dist(flask-security-too) >= 5.4
Requires: python3dist(flask-socketio) >= 5.4
Requires: python3dist(wtforms) >= 3
Requires: (python3dist(passlib) >= 1 with python3dist(passlib) < 2)
Requires: python3dist(pytz) >= 2024
Requires: (python3dist(sqlparse) >= 0 with python3dist(sqlparse) < 1)
Requires: python3dist(psutil) >= 5.9
Requires: python3dist(psycopg) >= 3.2.1
Requires: (python3dist(python-dateutil) >= 2 with python3dist(python-dateutil) < 3)
Requires: (python3dist(sqlalchemy) >= 2 with python3dist(sqlalchemy) < 3)
Requires: python3dist(bcrypt) >= 4.1
Requires: python3dist(cryptography) >= 43
Requires: (python3dist(sshtunnel) >= 0 with python3dist(sshtunnel) < 1)
Requires: (python3dist(ldap3) >= 2 with python3dist(ldap3) < 3)
Requires: python3dist(gssapi) >= 1.7
Requires: python3dist(user-agents) = 2.2
Requires: python3dist(authlib) >= 1.3
Requires: (python3dist(pyotp) >= 2 with python3dist(pyotp) < 3)
Requires: (python3dist(qrcode) >= 8 with python3dist(qrcode) < 9)
Requires: python3dist(boto3) >= 1.35
Requires: python3dist(urllib3) >= 1.25
Requires: python3dist(azure-mgmt-rdbms) >= 10.1
Requires: python3dist(azure-mgmt-resource) >= 23.1
Requires: python3dist(azure-mgmt-subscription) >= 3
Requires: python3dist(azure-identity) >= 1.17
Requires: (python3dist(google-api-python-client) >= 2 with python3dist(google-api-python-client) < 3)
Requires: python3dist(google-auth-oauthlib) >= 0.8
Requires: (python3dist(keyring) >= 25 with python3dist(keyring) < 26)
Requires: (python3dist(werkzeug) >= 3.1 with python3dist(werkzeug) < 3.2)
Requires: python3dist(typer-slim)
Requires: python3dist(setuptools) >= 74
Requires: (python3dist(jsonformatter) >= 0.3.4 with python3dist(jsonformatter) < 0.4)
Requires: (python3dist(libgravatar) >= 1 with python3dist(libgravatar) < 1.1)


# Undeclared dependencies
Requires:  python3-rich
Requires:  python3-libgravatar

Obsoletes: pgadmin3 < 1.23.0b-8
Provides:  pgadmin3 = %{version}-%{release}

%description
pgAdmin is the most popular and feature rich Open Source administration and development
platform for PostgreSQL, the most advanced Open Source database in the world.


%ifarch %{qt6_qtwebengine_arches}
%package qt
Summary:        Unofficial Qt runtime for pgadmin4
Requires:       %{name} = %{version}-%{release}
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel

%description qt
This package contains an unofficial Qt runtime for pgadmin4.
%endif


%package httpd
Summary:        Apache/WSGI configuration for pgadmin4
Requires:       python3-mod_wsgi
Requires:       %{name} = %{version}-%{release}

%description httpd
This package contains the Apache/WSGI configuration for serving pgadmin4 from Apache.


%define lang_subpkg() \
%package langpack-%{1}\
Summary:       %{2} language data for %{name}\
BuildArch:     noarch\
Requires:      %{name} = %{version}-%{release}\
Supplements:   (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description langpack-%{1}\
%{2} language data for %{name}.\
\
%files langpack-%{1}\
%{_prefix}/lib/%{name}/pgadmin/translations/%{1}/

%lang_subpkg cs Czech
%lang_subpkg de German
%lang_subpkg es Spanish
%lang_subpkg fr French
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg ko Korean
%lang_subpkg pl Polish
%lang_subpkg ru Russian


%generate_buildrequires
%pyproject_buildrequires -N requirements.txt


%prep
%setup -q -a1
%autopatch -M99 -p1

sed -i 's|Exec=.*|Exec=%{_bindir}/%{name}-qt|' pkg/linux/%{name}.desktop
cp -a %{SOURCE2} .

# Use system optipng, remove bundled source code
find .package-cache -name optipng.tar.gz -delete
ln -s %{_bindir}/optipng $(readlink -f .package-cache/v6/npm-optipng-bin-*/node_modules/optipng-bin/vendor)/optipng

# Update bundled mozjpeg
mozjpeg_dir=$(readlink -f .package-cache/v6/npm-mozjpeg-*/node_modules/mozjpeg/)
cp -a %SOURCE8 ${mozjpeg_dir}/vendor/source/mozjpeg.tar.gz
%patch 100 -p0 -d ${mozjpeg_dir}/lib


%build
(
cd web
cp -a %{SOURCE3} yarn.lock
YARN_CACHE_FOLDER="$PWD/../.package-cache" yarn install --offline
yarn run bundle
rm -rf node_modules
)

%ifarch %{qt6_qtwebengine_arches}
g++ -o %{name}-qt %{SOURCE4} %{optflags} $(pkg-config --cflags --libs Qt6Core Qt6Widgets Qt6Network Qt6WebEngineCore Qt6WebEngineWidgets)
%endif
make docs PYTHON=%{__python3} SPHINXBUILD=sphinx-build


%install
mkdir -p %{buildroot}%{_prefix}/lib/
cp -a web %{buildroot}%{_prefix}/lib/%{name}

# Local config
cat > %{buildroot}%{_prefix}/lib/%{name}/config_local.py <<EOF
from config import *
HELP_PATH = '%{_defaultdocdir}/%{name}/html/'
EOF

%ifarch %{qt6_qtwebengine_arches}
for size in 16 32 48 64 128; do
    install -Dpm 0644 pkg/linux/%{name}-${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
install -Dpm 0755 %{name}-qt %{buildroot}%{_bindir}/%{name}-qt
install -Dpm 0644 pkg/linux/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_metainfodir}/org.postgresql.pgadmin4.metainfo.xml
install -Dpm 0644 %{SOURCE6} %{buildroot}%{_datadir}/pgadmin4-qt/pgadmin4-qt.svg
%endif

# Apache/WSGI config
mkdir -p %{buildroot}%{_localstatedir}/lib/pgadmin
mkdir -p %{buildroot}%{_localstatedir}/log/pgadmin
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/httpd/conf.d/pgadmin4.conf



%check
%ifarch %{qt6_qtwebengine_arches}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.postgresql.pgadmin4.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%endif


%files
%license LICENSE %{name}-%{version}-vendor-licenses.txt
%doc docs/en_US/_build/html README.md
%{_prefix}/lib/%{name}
# Packaged by separate langpack subpackages
%exclude %{_prefix}/lib/%{name}/pgadmin/translations/*

%ifarch %{qt6_qtwebengine_arches}
%files qt
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pgadmin4-qt/
%{_metainfodir}/org.postgresql.pgadmin4.metainfo.xml
%endif

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/pgadmin4.conf
%attr(0700,apache,apache) %dir %{_localstatedir}/lib/pgadmin
%attr(0700,apache,apache) %dir %{_localstatedir}/log/pgadmin


%changelog
* Thu Feb 06 2025 Sandro Mani <manisandro@gmail.com> - 9.0-1
- Update to 9.0

* Sat Feb 01 2025 Sandro Mani <manisandro@gmail.com> - 8.14-6
- Relax pytz requires

* Sun Jan 19 2025 Sandro Mani <manisandro@gmail.com> - 8.14-5
- Relax boto3 requires

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 28 2024 Sandro Mani <manisandro@gmail.com> - 8.14-3
- Relax authlib requires

* Thu Dec 19 2024 Sandro Mani <manisandro@gmail.com> - 8.14-2
- Relax flask-socketio requires

* Fri Dec 13 2024 Sandro Mani <manisandro@gmail.com> - 8.14-1
- Update to 8.14

* Sun Nov 24 2024 Sandro Mani <manisandro@gmail.com> - 8.13-2
- Relax flask requires

* Fri Nov 15 2024 Sandro Mani <manisandro@gmail.com> - 8.13-1
- Update to 8.13

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 8.12-5
- Relax werkzeug requirement

* Mon Oct 21 2024 Sandro Mani <manisandro@gmail.com> - 8.12-4
- Grant clipboard paste access to WebEngineView in pgadmin4-qt

* Fri Oct 18 2024 Sandro Mani <manisandro@gmail.com> - 8.12-3
- Handle file downloads in pgadmin4-qt

* Thu Oct 03 2024 Sandro Mani <manisandro@gmail.com> - 8.12-2
- Relax socketio requirement

* Tue Sep 24 2024 Sandro Mani <manisandro@gmail.com> - 8.12-1
- Update to 8.12

* Thu Sep 05 2024 Sandro Mani <manisandro@gmail.com> - 8.11-2
- Revert react-data-grid update

* Fri Aug 23 2024 Sandro Mani <manisandro@gmail.com> - 8.11-1
- Update to 8.11

* Wed Aug 21 2024 Sandro Mani <manisandro@gmail.com> - 8.10-5
- Relax cryptography and flasksecurity-too requirements

* Sun Aug 18 2024 Sandro Mani <manisandro@gmail.com> - 8.10-4
- Relax boto3 requires

* Thu Aug 01 2024 Sandro Mani <manisandro@gmail.com> - 8.10-3
- Add Requires: python3-libgravatar

* Thu Aug 01 2024 Sandro Mani <manisandro@gmail.com> - 8.10-2
- Drop eventlet requires

* Wed Jul 31 2024 Sandro Mani <manisandro@gmail.com> - 8.10-1
- Update to 8.10

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Sandro Mani <manisandro@gmail.com> - 8.9-1
- Update to 8.9

* Mon Jun 03 2024 Sandro Mani <manisandro@gmail.com> - 8.7-1
- Update to 8.7

* Fri May 03 2024 Sandro Mani <manisandro@gmail.com> - 8.6-1
- Update to 8.6

* Sat Apr 13 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 8.5-2
- Adjust typer dependency for typer 0.12.1

* Thu Apr 11 2024 Sandro Mani <manisandro@gmail.com> - 8.5-1
- Update to 8.5

* Wed Mar 27 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 8.4-3
- Stop upper-bounding the version of python-typer

* Thu Mar 14 2024 Sandro Mani <manisandro@gmail.com> - 8.4-2
- Update vendored libraries for newer follow-redirects, fixes CVE-2024-28849

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 8.4-1
- Update to 8.4

* Sun Feb 25 2024 Sandro Mani <manisandro@gmail.com> - 8.3-4
- Require: python3-keyring

* Thu Feb 22 2024 Sandro Mani <manisandro@gmail.com> - 8.3-3
- Add pgadmin4_no-get-csrf.patch

* Mon Feb 19 2024 Sandro Mani <manisandro@gmail.com> - 8.3-2
- Relax bcrypt requirement

* Wed Feb 14 2024 Sandro Mani <manisandro@gmail.com> - 8.3-1
- Update to 8.3

* Sat Feb 03 2024 Sandro Mani <manisandro@gmail.com> - 8.2-4
- Relax pytz requirement

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Sandro Mani <manisandro@gmail.com> - 8.2-1
- Update to 8.2

* Thu Jan 11 2024 Sandro Mani <manisandro@gmail.com> - 8.1-2
- Relax authlib requires

* Mon Dec 18 2023 Sandro Mani <manisandro@gmail.com> - 8.1-1
- Update to 8.1

* Thu Nov 30 2023 Sandro Mani <manisandro@gmail.com> - 8.0-1
- Update to 8.0

* Thu Nov 16 2023 Sandro Mani <manisandro@gmail.com> - 7.8-3
- Relax boto3 and botocore requirements

* Mon Nov 13 2023 Sandro Mani <manisandro@gmail.com> - 7.8-2
- Switch to qt6

* Sun Oct 22 2023 Sandro Mani <manisandro@gmail.com> - 7.8-1
- Update to 7.8

* Sat Sep 30 2023 Sandro Mani <manisandro@gmail.com> - 7.7-2
- Relax flask-wtf requires

* Mon Sep 25 2023 Sandro Mani <manisandro@gmail.com> - 7.7-1
- Update to 7.7

* Wed Sep 13 2023 Sandro Mani <manisandro@gmail.com> - 7.6-3
- Relax python-keyring requires

* Sun Aug 27 2023 Sandro Mani <manisandro@gmail.com> - 7.6-2
- Add pgadmin4_sqlalchemy1.patch

* Sat Aug 26 2023 Sandro Mani <manisandro@gmail.com> - 7.6-1
- Update to 7.6

* Tue Aug 15 2023 Sandro Mani <manisandro@gmail.com> - 7.5-1
- Update to 7.5

* Thu Aug 10 2023 Sandro Mani <manisandro@gmail.com> - 7.0-3
- Update Requires

* Thu Aug 10 2023 Sandro Mani <manisandro@gmail.com> - 7.0-2
- Relax python-cryptography version constraint

* Fri Aug 04 2023 Sandro Mani <manisandro@gmail.com> - 7.0-1
- Update to 7.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 07 2023 Sandro Mani <manisandro@gmail.com> - 6.21-3
- Relax flask-sqlalchemy requirement

* Tue Mar 28 2023 Sandro Mani <manisandro@gmail.com> - 6.21-2
- Drop PGADMIN_INT_KEY env-var

* Wed Mar 15 2023 Sandro Mani <manisandro@gmail.com> - 6.21-1
- Update to 6.21

* Tue Feb 14 2023 Sandro Mani <manisandro@gmail.com> - 6.20-1
- Update to 6.20

* Thu Jan 19 2023 Sandro Mani <manisandro@gmail.com> - 6.19-1
- Update to 6.19

* Wed Jan 18 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 6.18-3
- Allow Flask-Migrate 4.x

* Tue Jan 03 2023 Sandro Mani <manisandro@gmail.com> - 6.18-2
- Backport fix for CVE-2021-35065 for bundled glob-parent

* Tue Jan 03 2023 Sandro Mani <manisandro@gmail.com> - 6.18-1
- Update to 6.18
- Update bundled mozjpeg (#2155769)

* Thu Dec 08 2022 Sandro Mani <manisandro@gmail.com> - 6.17-2
- Fix python-azure-mgmt-rdbms-10.2.0~b5+ compatibility

* Wed Dec 07 2022 Sandro Mani <manisandro@gmail.com> - 6.17-1
- Update to 6.17

* Sun Nov 27 2022 Sandro Mani <manisandro@gmail.com> - 6.16-2
- Fix incorrect path to log folder in pgadmin4-httpd

* Sat Nov 19 2022 Sandro Mani <manisandro@gmail.com> - 6.16-1
- Update to 6.16

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 6.15-3
- Fix window icon on Wayland

* Thu Nov 10 2022 Sandro Mani <manisandro@gmail.com> - 6.15-2
- Re-add pgadmin4_username.patch

* Tue Nov 08 2022 Sandro Mani <manisandro@gmail.com> - 6.15-1
- Update to 6.15

* Tue Oct 04 2022 Sandro Mani <manisandro@gmail.com> - 6.14-2
- Re-add pgadmin4_username.patch

* Fri Sep 23 2022 Sandro Mani <manisandro@gmail.com> - 6.14-1
- Update to 6.14

* Tue Sep 06 2022 Sandro Mani <manisandro@gmail.com> - 6.13-4
- Add pgadmin4_username.patch

* Mon Sep 05 2022 Sandro Mani <manisandro@gmail.com> - 6.13-3
- Re-add pgadmin4_flask22.patch

* Sun Sep 04 2022 Sandro Mani <manisandro@gmail.com> - 6.13-2
- Relax werkzeug requires

* Tue Aug 30 2022 Sandro Mani <manisandro@gmail.com> - 6.13-1
- Update to 6.13

* Sat Aug 06 2022 Sandro Mani <manisandro@gmail.com> - 6.12-4
- Add patch for Flask 2.2+ compatibility

* Thu Aug 04 2022 Sandro Mani <manisandro@gmail.com> - 6.12-3
- Relax werkzeug requires

* Mon Aug 01 2022 Sandro Mani <manisandro@gmail.com> - 6.12-2
- Rebuild (python-werkzeug)

* Fri Jul 29 2022 Sandro Mani <manisandro@gmail.com> - 6.12-1
- Update to 6.12

* Wed Jul 27 2022 Sandro Mani <manisandro@gmail.com> - 6.11-1
- Update to 6.11

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 08 2022 Sandro Mani <manisandro@gmail.com> - 6.9-4
- Grant clipboard access to pgadmin4-qt

* Mon May 30 2022 Sandro Mani <manisandro@gmail.com> - 6.9-3
- Add httpd subpackage

* Mon May 30 2022 Sandro Mani <manisandro@gmail.com> - 6.9-2
- Relax eventlet requires

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 6.9-1
- Update to 6.9

* Sat Apr 16 2022 Sandro Mani <manisandro@gmail.com> - 6.8-3
- Regenerate requires

* Fri Apr 15 2022 Sandro Mani <manisandro@gmail.com> - 6.8-2
- Relax authlib requires

* Thu Apr 07 2022 Sandro Mani <manisandro@gmail.com> - 6.8-1
- Update to 6.8

* Tue Mar 22 2022 Sandro Mani <manisandro@gmail.com> - 6.7-3
- Relax pytz requirement

* Tue Mar 15 2022 Sandro Mani <manisandro@gmail.com> - 6.7-2
- Fix requires

* Mon Mar 14 2022 Sandro Mani <manisandro@gmail.com> - 6.7-1
- Update to 6.7

* Sat Feb 12 2022 Sandro Mani <manisandro@gmail.com> - 6.5-1
- Update to 6.5

* Wed Feb 09 2022 Sandro Mani <manisandro@gmail.com> - 6.4-9
- ExcludeArch i686 and armv7hl rather than building without terser optimization
- Ship config_local.py rather than patching original config
- Rename pgadmin4 runtime binary to pgadmin4-qt
- Use system pngquant / optipng

* Tue Feb 08 2022 Sandro Mani <manisandro@gmail.com> - 6.4-8
- Add info dialog regarding unofficial qt runtime

* Tue Feb 01 2022 Sandro Mani <manisandro@gmail.com> - 6.4-7
- Split off unofficial qt runtime in separate subpackage

* Tue Feb 01 2022 Sandro Mani <manisandro@gmail.com> - 6.4-6
- Don't override SERVER_MODE globally, but set in pgadmin wrapper, and also set
  key in wrapper

* Tue Feb 01 2022 Sandro Mani <manisandro@gmail.com> - 6.4-5
- Remove SECRET_KEY hunk from pgadmin4.patch

* Tue Feb 01 2022 Sandro Mani <manisandro@gmail.com> - 6.4-4
- Add obsoletes/provides for pgadmin3

* Tue Jan 25 2022 Sandro Mani <manisandro@gmail.com> - 6.4-3
- Generate and add %%{name}-%%{version}-vendor-licenses.txt

* Tue Jan 25 2022 Sandro Mani <manisandro@gmail.com> - 6.4-2
- Add splash screen

* Thu Jan 13 2022 Sandro Mani <manisandro@gmail.com> - 6.4-1
- Update to 6.4

* Fri Dec 24 2021 Sandro Mani <manisandro@gmail.com> - 6.3-2
- Update pgadmin4.cpp

* Fri Dec 17 2021 Sandro Mani <manisandro@gmail.com> - 6.3-1
- Update to 6.3

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 6.3-0.1.git3a87e05
- Initial package
