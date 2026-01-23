Name:           undbx
Version:        0.21
Release:        %autorelease
Summary:        Outlook Express .dbx files extractor
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/ZungBang/undbx
Source0:        https://github.com/ZungBang/undbx/archive/undbx-%{version}.tar.gz

# https://github.com/ZungBang/undbx/pull/3
Patch0:         0001-Adjust-strncpy-call-to-not-use-string-length.patch

BuildRequires: make
BuildRequires:  gcc

%define _pkg_extra_cflags -Wno-error=unused-but-set-variable

%description
UnDBX is a tool to extract, recover and undelete e-mail messages from 
Outlook Express .dbx file.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc README.rst
%license COPYING
%{_bindir}/undbx
%exclude %{_bindir}/undbx.hta

%changelog
%autochangelog
