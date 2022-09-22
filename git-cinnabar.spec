#global rcver b4
%global bundled_git_version 2.37.1
%global gitexecdir %{_libexecdir}/git-core
%global _python_bytecompile_extra 0

Name:           git-cinnabar
Version:        0.5.10
Release:        %autorelease
Summary:        Git remote helper to interact with mercurial repositories

License:        GPLv2
URL:            https://github.com/glandium/git-cinnabar
Source0:        https://github.com/glandium/%{name}/archive/%{version}%{?rcver}/%{name}-%{version}%{?rcver}.tar.gz
Source1:        https://mirrors.edge.kernel.org/pub/software/scm/git/git-%{bundled_git_version}.tar.xz
# hg clone https://hg.mozilla.org/users/mh_glandium.org/jqplot &&
# cd jqplot &&
# hg bundle --all ../jqplot$(hg id -i).hg
Source2:        jqplot-e8af8a37f0f1.hg
# Skip stuff that's not relevant for a tarball.
Patch:          0001-Skip-version-checks.patch
# Shebangs must match package requirements.
Patch:          0002-Make-Python-shebangs-explicit.patch
# https://github.com/glandium/git-cinnabar/pull/305
Patch:          0003-Fix-compatibility-with-Python-3.11.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  python3-devel
BuildRequires:  hg >= 1.9
# Bundled git requirements:
BuildRequires:  git
BuildRequires:  libcurl-devel
BuildRequires:  zlib-devel >= 1.2

Requires:       git-core
Requires:       hg >= 1.9

Provides:       bundled(git) = %{bundled_git_version}

%description
git-cinnabar is a git remote helper to interact with mercurial repositories.
Contrary to other such helpers, it doesn't use a local mercurial clone under
the hood, although it currently does require mercurial to be installed for some
of its libraries.


%prep
%autosetup -p1 -n %{name}-%{version}%{?rcver}
%setup -D -T -n %{name}-%{version}%{?rcver} -q -a 1
rmdir git-core
mv git-%{bundled_git_version} git-core

# Use these same options for every invocation of 'make'.
# Otherwise it will rebuild in %%install due to flags changes.
# Pipe to tee to aid confirmation/verification of settings.
cat << \EOF | tee config.mak
V = 1
CFLAGS = %{build_cflags}
LDFLAGS = %{build_ldflags}
NEEDS_CRYPTO_WITH_SSL = 1
USE_LIBPCRE = 1
ETC_GITCONFIG = %{_sysconfdir}/gitconfig
INSTALL_SYMLINKS = 1
GITWEB_PROJECTROOT = %{_localstatedir}/lib/git
GNU_ROFF = 1
NO_PERL_CPAN_FALLBACKS = 1
NO_PYTHON = 1
htmldir = %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
prefix = %{_prefix}
perllibdir = %{perl_vendorlib}
gitwebdir = %{_localstatedir}/www/git

# Test options
DEFAULT_TEST_TARGET = prove
GIT_PROVE_OPTS = --verbose --normalize %{?_smp_mflags} --formatter=TAP::Formatter::File
GIT_TEST_OPTS = -x --verbose-log
EOF


%build
%make_build helper


%install
# Can't make_install because it tries to build all of git.
install -d %{buildroot}%{gitexecdir}
install -p -m 0755 git-cinnabar %{buildroot}%{gitexecdir}
install -p -m 0755 git-cinnabar-helper %{buildroot}%{gitexecdir}
install -p -m 0755 git-remote-hg %{buildroot}%{gitexecdir}
install -d %{buildroot}%{gitexecdir}/cinnabar
install -p -m 0644 cinnabar/*.py %{buildroot}%{gitexecdir}/cinnabar
install -d %{buildroot}%{gitexecdir}/cinnabar/cmd
install -p -m 0644 cinnabar/cmd/*.py %{buildroot}%{gitexecdir}/cinnabar/cmd
install -d %{buildroot}%{gitexecdir}/cinnabar/hg
install -p -m 0644 cinnabar/hg/*.py %{buildroot}%{gitexecdir}/cinnabar/hg

%py_byte_compile %{python3} %{buildroot}%{gitexecdir}/cinnabar


%check
# Silence a git warning.
git config --global init.defaultBranch main
# Check the installed copies.
mkdir gitexecdir
for f in %{gitexecdir}/* %{buildroot}%{gitexecdir}/*; do
    ln -s $f gitexecdir/
done
export GIT_EXEC_PATH=$PWD/gitexecdir
rm -r cinnabar
ln -s %{buildroot}%{gitexecdir}/cinnabar

%{python3} -m unittest discover -v -s tests/ -p '*.py'
make -f CI/tests.mk REPO=%SOURCE2 check check-graft


%files
%doc README.md
%license COPYING
%{gitexecdir}/git-cinnabar
%{gitexecdir}/git-cinnabar-helper
%{gitexecdir}/git-remote-hg
%{gitexecdir}/cinnabar


%changelog
%autochangelog
