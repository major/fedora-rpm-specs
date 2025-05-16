# Do we build in/for the distro or in copr?
%bcond distrobuild 1

# We used to set these based on fedora/rhel versions. Keep them in case for now.
%bcond tests 1
%bcond sfsexp 1

# comparing {_emacs_version} in macros does not work well
# so we catch the major version bumps ;)
# read "with emacs at least"
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
%global with_emacs28 1
%endif
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10
%global with_emacs29 1
%endif

Name:           notmuch
Version:        0.39
Release:        %autorelease
Summary:        System for indexing, searching, and tagging email
License:        GPL-3.0-or-later
URL:            https://notmuchmail.org/
Source0:        https://notmuchmail.org/releases/notmuch-%{version}.tar.xz
Source1:        https://notmuchmail.org/releases/notmuch-%{version}.tar.xz.asc
# imported from `gpg --locate-external-key david@tethera.net`
# cross checked with `gpg --keyserver keyring.debian.org --recv-key 7E4E65C8720B706B`
# as per author's instructions on the mailing-list
# `gpg --export --export-options export-minimal 7A18807F100A4570C59684207E4E65C8720B706B > gpgkey-7A18807F100A4570C59684207E4E65C8720B706B.gpg`
Source2:        gpgkey-7A18807F100A4570C59684207E4E65C8720B706B.gpg
Patch:          0001-test-allow-to-use-full-scan.patch
Patch:          0002-test-use-NOTMUCH_NEW-consistently.patch
Patch:          0003-test-use-NOTMUCH_NEW_OPTIONS-in-atomicity.py.patch
Patch:          0004-test-correct-comparison-order-in-T380.patch
Patch:          0005-test-do-not-pass-T380.1-for-the-wrong-reasons.patch
Patch:          0006-test-reword-T380.2-to-be-clearer.patch
Patch:          0007-test-set-up-the-outcount-for-T380.1.patch

BuildRequires:  make
%if 0%{?fedora} >= 41
BuildRequires:  bash-completion-devel
%else
BuildRequires:  bash-completion
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  emacs
BuildRequires:  emacs-el
BuildRequires:  emacs-nox
Buildrequires:  gcc gcc-c++
BuildRequires:  libtool
BuildRequires:  doxygen
BuildRequires:  texinfo
BuildRequires:  gnupg2
BuildRequires:  gnupg2-smime
BuildRequires:  gmime30-devel
BuildRequires:  libtalloc-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  ruby-devel
%if %{with sfsexp}
BuildRequires:  pkgconfig(sfsexp)
%endif
BuildRequires:  xapian-core-devel
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx

BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
# Not available on *EL, skip some tests there:
  %if 0%{?fedora}
BuildRequires:  python3-pytest-shutil
  %endif
BuildRequires:  python3-cffi
# dtach not available on *EL, skip some tests there;
# copr only: use mjg/dtach-epel
  %if 0%{?fedora} || %{without distrobuild}
BuildRequires:  dtach
  %endif
BuildRequires:  gdb
  %if %{with sfsexp}
BuildRequires:  git-core
  %endif
BuildRequires:  man
BuildRequires:  openssl
# You might also want to rebuild with valgrind-devel libasan libasan-static.
%endif

Requires(post): /sbin/install-info
Requires(postun): /sbin/install-info

%description
Fast system for indexing, searching, and tagging email.  Even if you
receive 12000 messages per month or have on the order of millions of
messages that you've been saving for decades, Notmuch will be able to
quickly search all of it.

Notmuch is not much of an email program. It doesn't receive messages
(no POP or IMAP support). It doesn't send messages (no mail composer,
no network code at all). And for what it does do (email search) that
work is provided by an external library, Xapian. So if Notmuch
provides no user interface and Xapian does all the heavy lifting, then
what's left here? Not much.

%package    devel
Summary:    Development libraries and header files for the Notmuch library
Requires:   %{name} = %{version}-%{release}

%description devel
Notmuch-devel contains the development libraries and header files for
Notmuch email program.  These libraries and header files are
necessary if you plan to do development using Notmuch.

Install notmuch-devel if you are developing C programs which will use the
Notmuch library.  You'll also need to install the notmuch package.

%if %{with sfsexp}
%package    git
Summary:    Manage notmuch tags with git
Requires:   %{name} = %{version}-%{release}
Requires:   git-core
Recommends: python3-notmuch2

%description git
This package contains a simple tool to save, restore, and synchronize
notmuch tags via git repositories.
%endif

%package -n emacs-notmuch
Summary:    Not much support for Emacs
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   emacs(bin) >= %{_emacs_version}

%description -n emacs-notmuch
%{summary}.

%package -n python3-notmuch2
Summary:    Python3 bindings for notmuch (cffi)
Requires:   %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-notmuch2}

Requires:   python3
# Keep these as long as we need to provide an upgrade path:
Obsoletes:  python-notmuch < 0.39~rc2-1
Obsoletes:  python3-notmuch < 0.39~rc2-1

%description -n python3-notmuch2
%{summary}.

%package -n ruby-notmuch
Summary:    Ruby bindings for notmuch
Requires:   %{name} = %{version}-%{release}

%description -n ruby-notmuch
%{summary}.

%package    mutt
Summary:    Notmuch (of a) helper for Mutt
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Requires:   perl(Term::ReadLine::Gnu)

%description mutt
notmuch-mutt provide integration among the Mutt mail user agent and
the Notmuch mail indexer.

%package    vim
Summary:    A Vim plugin for notmuch
Requires:   ruby-%{name} = %{version}-%{release}
Requires:   rubygem-mail
Requires:   vim-enhanced
# Required for updating helptags in scriptlets.
Requires(post):    vim-enhanced
Requires(postun):  vim-enhanced

%description vim
notmuch-vim is a Vim plugin that provides a fully usable mail client
interface, utilizing the notmuch framework.

%prep
%if %{with distrobuild}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
%else
# unversioned dir for git build, no check
%autosetup -n notmuch -p1
%endif

%build
# DEBUG mtime/stat
%configure --emacslispdir=%{_emacs_sitelispdir}
%make_build CFLAGS="$RPM_OPT_FLAGS -fPIC"

# Build the python cffi bindings
pushd bindings/python-cffi
%py3_build
popd

# Build notmuch-mutt
pushd contrib/notmuch-mutt
    make
popd

%if %{with tests}
%check
# armv7hl pulls in libasan but we build without, and should test without it.
NOTMUCH_SKIP_TESTS="asan"
# notmuch-git and its tests require sfsexp.
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS%{!?with_sfsexp: git}"
# T460-emacs-tree.14 leads to sporadic failures with emacs 29
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS%{?with_emacs29: emacs-tree.14}"
# T460-emacs-tree.23 uses outline-cycle-buffer which requires emacs 28
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS%{!?with_emacs28: emacs-tree.23}"
# At least on koji/copr, test suite suffers from race conditions when parallelised.
# At least some rhel builds show mtime/stat related Heisenbugs when
# notmuch new takes shortcuts, so enforce --full-scan there.
NOTMUCH_SKIP_TESTS="$NOTMUCH_SKIP_TESTS" \
NOTMUCH_TEST_SERIALIZE="yesplease" \
make test V=1 %{?rhel:NOTMUCH_TEST_FULLSCAN=1}
%endif

%install
%make_install

# Enable dynamic library stripping.
find %{buildroot}%{_libdir} -name *.so* -exec chmod 755 {} \;

%if %{with sfsexp}
install -m0755 notmuch-git nmbug %{buildroot}%{_bindir}/
%endif

# Install the python cffi bindings and documentation
pushd bindings/python-cffi
%py3_install
popd

# Install the ruby bindings
pushd bindings/ruby
    make install DESTDIR=%{buildroot}
popd

# Install notmuch-mutt
install -m0755 contrib/notmuch-mutt/notmuch-mutt \
    %{buildroot}%{_bindir}/notmuch-mutt
install -m0644 contrib/notmuch-mutt/notmuch-mutt.1 \
    %{buildroot}%{_mandir}/man1/notmuch-mutt.1

# Install notmuch-vim
pushd vim
    make install DESTDIR=%{buildroot} prefix="%{_datadir}/vim/vimfiles"
popd

%if %{without sfsexp}
# Do not install notmuch-git which requires sfsexp
rm -f %{buildroot}%{_mandir}/man1/nmbug.1*
rm -f %{buildroot}%{_mandir}/man1/notmuch-git.1*
rm -f %{buildroot}%{_infodir}/nmbug.info*
rm -f %{buildroot}%{_infodir}/notmuch-git.info*
%endif

rm -f %{buildroot}/%{_datadir}/applications/mimeinfo.cache
rm -f %{buildroot}%{_infodir}/dir

%post vim
cd %{_datadir}/vim/vimfiles/doc
vim -u NONE -esX -c "helptags ." -c quit

%postun vim
cd %{_datadir}/vim/vimfiles/doc
vim -u NONE -esX -c "helptags ." -c quit

%files
%doc AUTHORS COPYING COPYING-GPL-3 README
%{_datadir}/zsh/site-functions/_notmuch
%{_datadir}/zsh/site-functions/_email-notmuch
%{_datadir}/bash-completion/completions/notmuch
%{_bindir}/notmuch
%{_libdir}/libnotmuch.so.5*
%{_mandir}/man1/notmuch.1*
%{_mandir}/man1/notmuch-address.1*
%{_mandir}/man1/notmuch-compact.1*
%{_mandir}/man1/notmuch-config.1*
%{_mandir}/man1/notmuch-count.1*
%{_mandir}/man1/notmuch-dump.1*
%{_mandir}/man1/notmuch-insert.1*
%{_mandir}/man1/notmuch-new.1*
%{_mandir}/man1/notmuch-reindex.1*
%{_mandir}/man1/notmuch-reply.1*
%{_mandir}/man1/notmuch-restore.1*
%{_mandir}/man1/notmuch-search.1*
%{_mandir}/man1/notmuch-setup.1*
%{_mandir}/man1/notmuch-show.1*
%{_mandir}/man1/notmuch-tag.1*
%{_mandir}/man5/notmuch-hooks.5*
%{_mandir}/man7/notmuch-properties.7*
%{_mandir}/man7/notmuch-search-terms.7*
%{_mandir}/man7/notmuch-sexp-queries.7*
%{_infodir}/notmuch.info*
%{_infodir}/notmuch-address.info*
%{_infodir}/notmuch-compact.info*
%{_infodir}/notmuch-config.info*
%{_infodir}/notmuch-count.info*
%{_infodir}/notmuch-dump.info*
%{_infodir}/notmuch-hooks.info*
%{_infodir}/notmuch-insert.info*
%{_infodir}/notmuch-new.info*
%{_infodir}/notmuch-properties.info*
%{_infodir}/notmuch-reindex.info*
%{_infodir}/notmuch-reply.info*
%{_infodir}/notmuch-restore.info*
%{_infodir}/notmuch-search-terms.info*
%{_infodir}/notmuch-search.info*
%{_infodir}/notmuch-setup.info*
%{_infodir}/notmuch-sexp-queries.info*
%{_infodir}/notmuch-show.info*
%{_infodir}/notmuch-tag.info*

%files devel
%{_libdir}/libnotmuch.so
%{_includedir}/*
%{_mandir}/man3/notmuch*.3*

%if %{with sfsexp}
%files git
%{_bindir}/nmbug
%{_bindir}/notmuch-git
%{_mandir}/man1/nmbug.1*
%{_mandir}/man1/notmuch-git.1*
%{_infodir}/nmbug.info*
%{_infodir}/notmuch-git.info*
%endif

%files -n emacs-notmuch
%{_emacs_sitelispdir}/*.el
%{_emacs_sitelispdir}/*.elc
%{_emacs_sitelispdir}/notmuch-logo.svg
%{_datadir}/applications/notmuch-emacs-mua.desktop
%{_bindir}/notmuch-emacs-mua
%{_mandir}/man1/notmuch-emacs-mua.1*
%{_infodir}/notmuch-emacs-mua.info*
%{_infodir}/notmuch-emacs.info*

%files -n python3-notmuch2
%{python3_sitearch}/notmuch*

%files -n ruby-notmuch
%{ruby_vendorarchdir}/*

%files mutt
%{_bindir}/notmuch-mutt
%{_mandir}/man1/notmuch-mutt.1*

%files vim
%{_datadir}/vim/vimfiles/doc/notmuch.txt
%{_datadir}/vim/vimfiles/plugin/notmuch.vim
%{_datadir}/vim/vimfiles/syntax/notmuch-compose.vim
%{_datadir}/vim/vimfiles/syntax/notmuch-folders.vim
%{_datadir}/vim/vimfiles/syntax/notmuch-git-diff.vim
%{_datadir}/vim/vimfiles/syntax/notmuch-search.vim
%{_datadir}/vim/vimfiles/syntax/notmuch-show.vim

%changelog
%autochangelog
