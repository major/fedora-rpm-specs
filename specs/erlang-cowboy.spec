%global realname cowboy

Name:		erlang-%{realname}
Version:	2.17.0
Release:	%autorelease
BuildArch:	noarch
Summary:	Small, fast, modular HTTP server written in Erlang
License:	ISC
URL:		https://github.com/ninenines/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-cowlib
BuildRequires:	erlang-ct_helper
BuildRequires:	erlang-gun
BuildRequires:	erlang-ranch
BuildRequires:  erlang-rebar3
# For building docs
BuildRequires:	asciidoc
BuildRequires:	dblatex
BuildRequires:	libxml2
BuildRequires:	texlive-upquote

%description
%{summary}.

%package doc
Summary: Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -p 1 -n %{realname}-%{version}

%build
%{erlang3_compile}
# Building docs
a2x -v -f pdf CONTRIBUTING.asciidoc
a2x -v -f pdf doc/src/guide/book.asciidoc && mv doc/src/guide/book.pdf doc/guide.pdf
a2x -v -f chunked doc/src/guide/book.asciidoc && mv doc/src/guide/book.chunked/ doc/html/
# FIXME broken right now
# for f in doc/src/manual/*.asciidoc ; do a2x -v -f manpage $f ; done

%install
%{erlang3_install}

# man-pages installation
# FIXME broken right now
#install -d %{buildroot}%{_mandir}/man3
#install -d %{buildroot}%{_mandir}/man7
#for manfile in `ls doc/src/manual/*.3`
#do
#	install -p -m 0644 $manfile %{buildroot}%{_mandir}/man3/
#done
#for manfile in `ls doc/src/manual/*.7`
#do
#	install -p -m 0644 $manfile %{buildroot}%{_mandir}/man7/
#done

%check
# FIXME broken - need to investigate
#%%{erlang3_test}

%files
%license LICENSE
%doc README.asciidoc
%{erlang_appdir}/
#%%{_mandir}/man3/*
#%%{_mandir}/man7/*

%files doc
%doc CONTRIBUTING.pdf doc/guide.pdf doc/html examples/

%changelog
%autochangelog
