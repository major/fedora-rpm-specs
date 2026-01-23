# All package versioning is found here:
# the actual version is composed from these below
#   bzrmajor:  main bzr version
#   Version: bzr version, add subrelease version here
%global brzmajor 3.3
%global brzminor .20

# Optional dependencies not packaged or retired:
%bcond fastimport 0
%bcond github 0

Name:           breezy
Version:        %{brzmajor}%{?brzminor}
Release:        %autorelease
Summary:        Friendly distributed version control system

# breezy is GPL-2.0-or-later, but it has Rust dependencies
# Packaged LICENSE.dependencies contains a full license breakdown
# Paste the the output of %%{cargo_license_summary} here:
#
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# GPL-2.0+
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        GPL-2.0-or-later AND (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND MIT AND (Unlicense OR MIT)
URL:            http://www.breezy-vcs.org/
Source0:        https://github.com/breezy-team/breezy/archive/brz-%{version}%{?brzrc}.tar.gz
Source1:        brz-icon-64.png

# Allow dulwich version 1
# https://github.com/breezy-team/breezy/pull/335
Patch:          dulwich1.patch

BuildRequires:  python3-devel
BuildRequires:  rust-packaging >= 21
BuildRequires:  zlib-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make

# This is the name of the command, note that it is brz, not bzr
Provides:       brz = %{version}-%{release}

# breezy is a fork of bzr and replaces it
Provides:       bzr = %{version}-%{release}
Obsoletes:      bzr < 3
Provides:       git-remote-bzr = %{version}-%{release}
Obsoletes:      git-remote-bzr < 3

# This is needed for launchpad support
Recommends:     breezy+launchpad

# Docs are not needed, but some might want them
Suggests:       %{name}-doc = %{version}-%{release}

%description
Breezy (brz) is a decentralized revision control system, designed to be easy
for developers and end users alike.

By default, Breezy provides support for both the Bazaar and Git file formats.


%pyproject_extras_subpkg -n breezy %{?with_fastimport:fastimport} git %{?with_github:github} launchpad pgp paramiko


%package doc
Summary:        Documentation for Breezy
License:        GPL-2.0-or-later
BuildArch:      noarch

%description doc
This package contains the documentation for the Breezy version control system.

%prep
%autosetup -p1 -n %{name}-brz-%{version}%{?brzrc}

%cargo_prep

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

# Don't strip debug symbols, we generate debuginfo packages
sed -i 's/Strip.All/Strip.No/' setup.py


%generate_buildrequires
%cargo_generate_buildrequires
%pyproject_buildrequires -x doc,%{?with_fastimport:,fastimport},git,%{?with_github:,github},launchpad,pgp,paramiko


%build
%pyproject_wheel

chmod a-x contrib/bash/brzbashprompt.sh

# Generate man pages (needed because pyproject_wheel doesn't run setup.py build_man)
%{__python3} tools/generate_docs.py man

# Build documents
make docs-sphinx PYTHON=%{__python3}
rm doc/*/_build/html/.buildinfo
rm -f doc/*/_build/html/_static/*/Makefile
pushd doc
for dir in *; do
  test -d $dir/_build/html && mv $dir/_build/html ../$dir
done
popd

# Add Rust licenses
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%pyproject_install
%pyproject_save_files -l breezy
chmod -R a+rX contrib
chmod 0644 contrib/debian/init.d
chmod 0644 contrib/bzr_ssh_path_limiter  # note the bzr here
chmod 0644 contrib/brz_access
chmod 0755 %{buildroot}%{python3_sitearch}/%{name}/*.so

install -Dpm 0644 contrib/bash/brz %{buildroot}%{bash_completions_dir}/brz
rm contrib/bash/brz

install -d %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/brz.png

# Install man pages manually
install -d %{buildroot}%{_mandir}/man1
install -m 0644 brz.1 %{buildroot}%{_mandir}/man1/
install -m 0644 breezy/git/git-remote-bzr.1 %{buildroot}%{_mandir}/man1/

# move git-remote-bzr to avoid conflict
mv %{buildroot}%{_bindir}/git-remote-bzr %{buildroot}%{_bindir}/git-remote-brz
mv %{buildroot}%{_mandir}/man1/git-remote-bzr.1 %{buildroot}%{_mandir}/man1/git-remote-brz.1

# backwards compatible symbolic links
ln -s brz %{buildroot}%{_bindir}/bzr
ln -s git-remote-brz %{buildroot}%{_bindir}/git-remote-bzr
echo ".so man1/brz.1" > %{buildroot}%{_mandir}/man1/bzr.1
echo ".so man1/git-remote-brz.1" > %{buildroot}%{_mandir}/man1/git-remote-bzr.1

# With older versions of setuptools-gettext, locales are generated to a weird
# directory; move them to datadir.
if [ -d %{buildroot}%{buildroot}%{_datadir}/locale ]
then
  mv %{buildroot}%{buildroot}%{_datadir}/locale %{buildroot}%{_datadir}
fi
%find_lang %{name}
cat %{name}.lang >> %{pyproject_files}


%check
# for now, at least run a basic smoke test to prevent undetected major breakages
# like https://bugzilla.redhat.com/2366194
export %{py3_test_envvars}
brz init-repo testrepo


%files -f %{pyproject_files}
%license LICENSE.dependencies
%doc NEWS README.rst TODO contrib/
%{_bindir}/brz
%{_bindir}/bzr-*-pack
%{_bindir}/git-remote-brz
%{_bindir}/bzr
%{_bindir}/git-remote-bzr
%{_mandir}/man1/*
%{bash_completions_dir}/brz
%{_datadir}/pixmaps/brz.png


%files doc
%license COPYING.txt LICENSE.dependencies
%doc en developers


%changelog
%autochangelog
