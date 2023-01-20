# All package versioning is found here:
# the actual version is composed from these below, including leading 0 for release candidates
#   bzrmajor:  main bzr version
#   Version: bzr version, add subrelease version here
#   bzrrc: release candidate version, if any, line starts with % for rc, # for stable releas (no %).
#   baserelease: rpm release number (0.N for rc candidates, N for stable releases)
%global brzmajor 3.2
%global brzminor .2
#global brzrc b6
%global baserelease 7

Name:           breezy
Version:        %{brzmajor}%{?brzminor}
Release:        %{baserelease}%{?brzrc:.}%{?brzrc}%{?dist}
Summary:        Friendly distributed version control system

License:        GPLv2+
URL:            http://www.breezy-vcs.org/
Source0:        https://launchpad.net/brz/%{brzmajor}/%{version}%{?brzrc}/+download/%{name}-%{version}%{?brzrc}.tar.gz
Source1:        https://launchpad.net/brz/%{brzmajor}/%{version}%{?brzrc}/+download/%{name}-%{version}%{?brzrc}.tar.gz.asc
Source2:        brz-icon-64.png

BuildRequires:  python3-devel
BuildRequires:  python3-configobj
BuildRequires:  python3-Cython
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-epytext
BuildRequires:  python3-setuptools
BuildRequires:  python-fastbencode
BuildRequires:  zlib-devel
BuildRequires:  bash-completion
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

Requires:       python3-paramiko

# This is the name of the command, note that it is brz, not bzr
Provides:       brz = %{version}-%{release}

# breezy is a fork of bzr and replaces it
Provides:       bzr = %{version}-%{release}
Obsoletes:      bzr < 3
Provides:       git-remote-bzr = %{version}-%{release}
Obsoletes:      git-remote-bzr < 3

# This is needed for launchpad support
Recommends:     python3-launchpadlib

# Docs are not needed, but some might want them
Suggests:       %{name}-doc = %{version}-%{release}

%description
Breezy (brz) is a decentralized revision control system, designed to be easy
for developers and end users alike.

By default, Breezy provides support for both the Bazaar and Git file formats.


%package doc
Summary:        Documentation for Breezy
BuildArch:      noarch

%description doc
This package contains the documentation for the Breezy version control system.

%prep
%autosetup -p0 -n %{name}-%{version}%{?brzrc}

# Remove unused shebangs
sed -i '1{/#![[:space:]]*\/usr\/bin\/\(python\|env\)/d}' \
    breezy/__main__.py \
    breezy/git/git_remote_helper.py \
    breezy/git/tests/test_git_remote_helper.py \
    breezy/plugins/bash_completion/bashcomp.py \
    breezy/plugins/zsh_completion/zshcomp.py \
    breezy/tests/ssl_certs/create_ssls.py \
    contrib/brz_access

# Remove Cython generated .c files
find . -name '*_pyx.c' -exec rm \{\} \;

%build
%py3_build

chmod a-x contrib/bash/brzbashprompt.sh

# Build documents
make docs-sphinx PYTHON=%{__python3}
rm doc/*/_build/html/.buildinfo
rm -f doc/*/_build/html/_static/*/Makefile
pushd doc
for dir in *; do
  test -d $dir/_build/html && mv $dir/_build/html ../$dir
done
popd


%install
%py3_install
chmod -R a+rX contrib
chmod 0644 contrib/debian/init.d
chmod 0644 contrib/bzr_ssh_path_limiter  # note the bzr here
chmod 0644 contrib/brz_access
chmod 0755 %{buildroot}%{python3_sitearch}/%{name}/*.so

bashcompdir=$(pkg-config --variable=completionsdir bash-completion)
install -Dpm 0644 contrib/bash/brz %{buildroot}$bashcompdir/brz
rm contrib/bash/brz

install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/brz.png

# weird man page location
mv %{buildroot}%{_prefix}/man %{buildroot}%{_datadir}

# move git-remote-bzr to avoid conflict
mv %{buildroot}%{_bindir}/git-remote-bzr %{buildroot}%{_bindir}/git-remote-brz
mv %{buildroot}%{_mandir}/man1/git-remote-bzr.1 %{buildroot}%{_mandir}/man1/git-remote-brz.1

# backwards compatible symbolic links
ln -s brz %{buildroot}%{_bindir}/bzr
ln -s git-remote-brz %{buildroot}%{_bindir}/git-remote-bzr
echo ".so man1/brz.1" > %{buildroot}%{_mandir}/man1/bzr.1
echo ".so man1/git-remote-brz.1" > %{buildroot}%{_mandir}/man1/git-remote-bzr.1

# locales: all the .po files have empty msgstrs, so this doesn't do anything
#mv %%{name}/locale %%{buildroot}%%{_datadir}
#%%find_lang %%{name}


%files
# ... -f %%{name}.lang
%license COPYING.txt
%doc NEWS README.rst TODO contrib/
%{_bindir}/brz
%{_bindir}/bzr-*-pack
%{_bindir}/git-remote-brz
%{_bindir}/bzr
%{_bindir}/git-remote-bzr
%{_mandir}/man1/*
%{python3_sitearch}/%{name}/
%{python3_sitearch}/*.egg-info/
%{_datadir}/bash-completion/
%{_datadir}/pixmaps/brz.png


%files doc
%license COPYING.txt
%doc en developers


%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.2-5
- Rebuilt for Python 3.11

* Tue Jun 07 2022 Ondrej Pohorelsky <opohorel@redhat.com> - 3.2.2-4
- Update to 3.2.2
- Resolves: #2070029

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Ondrej Pohorelsky <opohorel@redhat.com> - 3.2.1-1
- Update to 3.2.1
- Resolves: #1980401

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.0-2
- Rebuilt for Python 3.10

* Wed May 05 2021 Ondrej Pohorelsky <opohorel@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Ondrej Pohorelsky <opohorel@redhat.com> - 3.1.0-1
- Update to 3.1.0

* Thu Oct 22 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-5
- Replace bazaar in ELN as well

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 01 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-1
- Update to 3.0.2

* Thu Oct 24 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-4
- On Fedora 32+, replace bazaar with breezy
  https://fedoraproject.org/wiki/Changes/ReplaceBazaarWithBreezy

* Thu Oct 17 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-3
- Reenable all extension modules

* Thu Oct 10 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-2
- Disable the _static_tuple_c extension module to workaround Python 3.8 problems (#1760260)
- Other disabled modules depending on the above:
  _chk_map_pyx, _dirstate_helpers_pyx, _bencode_pyx, _btree_serializer_pyx

* Wed Sep 04 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.1-1
- Package breezy
