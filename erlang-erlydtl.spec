%global realname erlydtl
%global upstream erlydtl


Name:		erlang-%{realname}
Version:        0.14.0
Release:        %autorelease
BuildArch:      noarch
Summary:        Erlang implementation of the Django Template Language
License:        MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-erlydtl-0001-No-such-function-exported-gettext_compile-write_pret.patch
Patch2:		erlang-erlydtl-0002-No-such-function-exported-gettext_compile-fmt_filein.patch
Patch3:		erlang-erlydtl-0003-No-such-fun-gettext_compile-open_po_file-3.patch
Patch4:		erlang-erlydtl-0004-No-such-fun-gettext_compile-close_file-0.patch
Provides:       ErlyDTL = %{version}-%{release}
BuildRequires:  erlang-rebar3


%description
ErlyDTL is an Erlang implementation of the Django Template Language. The
erlydtl module compiles Django Template source code into Erlang bytecode. The
compiled template has a "render" function that takes a list of variables and
returns a fully rendered document.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang3_compile}


%install
%{erlang3_install}
cp -arv priv %{buildroot}/%{erlang_appdir}/


%check
# FIXME
#%%{erlang3_test -C rebar-tests.config}
#REBAR_CONFIG=./rebar-tests.config %%{erlang3_test}


%files
%license LICENSE
%doc CONTRIBUTING.md NEWS.md README.markdown README_I18N
%{erlang_appdir}/


%changelog
%autochangelog
