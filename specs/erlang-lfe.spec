%global realname lfe

Name:		erlang-%{realname}
Version:	2.2.0
Release:	%autorelease
Summary:	Lisp Flavoured Erlang
License:	Apache-2.0
URL:		https://github.com/lfe/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch:		erlang-lfe-0001-Restore-functions-removed-in-pre-R17-Erlang.patch
Patch:		erlang-lfe-0002-We-don-t-have-proper-yet.patch
BuildRequires:	emacs
BuildRequires:	erlang-proper
BuildRequires:	erlang-rebar3
BuildRequires:	gcc
Obsoletes:	emacs-erlang-lfe
Obsoletes:	emacs-erlang-lfe-el
Requires:	emacs-filesystem

%description
Lisp Flavoured Erlang, is a lisp syntax front-end to the Erlang
compiler. Code produced with it is compatible with "normal" Erlang
code. An LFE evaluator and shell is also included.

%prep
%autosetup -p 1 -n %{realname}-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
gcc c_src/lfeexec.c $CFLAGS -fPIC -c -o c_src/lfeexec.o
gcc c_src/lfeexec.o $LDFLAGS -o bin/lfeexec

emacs -L emacs/ -batch -f batch-byte-compile emacs/inferior-lfe.el emacs/lfe-mode.el emacs/lfe-indent.el

%install
%{erlang3_install}

install -m 0755 -d %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/bin
install -p -m 0755 -D bin/*  %{buildroot}%{_libdir}/erlang/lib/%{realname}-%{version}/bin/
install -m 0755 -d %{buildroot}/%{_bindir}
ln -s %{_libdir}/erlang/lib/%{realname}-%{version}/bin/{lfe,lfe-test,lfec,lfedoc,lfeexec,lfescript} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_emacs_sitelispdir}
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 emacs/inferior-lfe.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/inferior-lfe.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-mode.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-mode.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-indent.el %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-indent.elc %{buildroot}%{_emacs_sitelispdir}
install -p -m 0644 emacs/lfe-start.el %{buildroot}%{_emacs_sitestartdir}

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md doc/ examples/
%{_bindir}/lfe
%{_bindir}/lfe-test
%{_bindir}/lfec
%{_bindir}/lfedoc
%{_bindir}/lfeexec
%{_bindir}/lfescript
%{erlang_appdir}/
%{_emacs_sitelispdir}/inferior-lfe.el
%{_emacs_sitelispdir}/inferior-lfe.elc
%{_emacs_sitelispdir}/lfe-indent.el
%{_emacs_sitelispdir}/lfe-indent.elc
%{_emacs_sitelispdir}/lfe-mode.el
%{_emacs_sitelispdir}/lfe-mode.elc
%{_emacs_sitestartdir}/lfe-start.el

%changelog
%autochangelog
