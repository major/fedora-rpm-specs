# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

# 390x arch:
# Error in test case: 150_tag_config_invalid_tags.txt (top: actual; bottom:
# expected)
%ifnarch s390x
%if 0%{?fedora} >= 39 || 0%{?el8}
%bcond_without tests
%endif
%endif

%global cfgfile %{_datadir}/%{name}/%{name}

Name:           boxes
Version:        2.3.0
Release:        %autorelease
Summary:        Command line ASCII boxes unlimited!

License:        GPL-3.0-only
URL:            http://boxes.thomasjensen.com
Source0:        https://github.com/ascii-%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  vim-common
BuildRequires:  pkgconfig(ncurses)

%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends:     %{name}-vim = %{version}-%{release}
%endif

%description
Boxes is a command line program which draws, removes, and repairs ASCII art
boxes. It operates as a text filter. The generated boxes may even be removed
and repaired again if they were badly damaged by editing of the text inside.
Since boxes may be open on any side, boxes can also be used to create
(regional) comments in any programming language.

Boxes is useful for making the function headers in your programming language
look better, for spicing up news postings and emails, or just for decorating
documentation files. Since the drawn box is matched in size to your input
text, you can use boxes in scripts to dynamically add boxes around stuff.


%package        vim
BuildArch:      noarch

Summary:        Vim plugin for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       vim-enhanced

%description    vim
Vim plugin for %{name}.


%prep
%autosetup


%build
%set_build_flags
%make_build \
    CFLAGS_ADDTL='%{optflags}' \
    GLOBALCONF=%{cfgfile} \
    LDFLAGS_ADDTL='%{build_ldflags}' \
    debug \
    %{nil}


%if %{with tests}
%check
# https://github.com/ascii-boxes/boxes/issues/124
export TERM=xterm-color
%if 0%{?el8}
export LANG=en_US.UTF-8
%endif
%make_build test
%endif


%install
install -Dp -m 0755 out/%{name}     %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 %{name}-config  %{buildroot}%{cfgfile}
install -Dp -m 0644 doc/%{name}.1   %{buildroot}%{_mandir}/man1/%{name}.1
install -Dp -m 0644 %{name}.vim     %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/*.1*

%files vim
%{_datadir}/vim/vimfiles/syntax/%{name}.vim


%changelog
%autochangelog
