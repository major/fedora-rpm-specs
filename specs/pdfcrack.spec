%global _hardened_build 1

Name:           pdfcrack
Version:        0.20
Release:        %autorelease
Summary:        A Password Recovery Tool for PDF files


# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pdfcrack.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make


%description
PDFCrack is a GNU/Linux tool for recovering passwords and content
from PDF-files. It is small, command line driven without external
dependencies.

%prep
%autosetup


%build
%make_build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -pm0755 %{name} $RPM_BUILD_ROOT%{_bindir}/
install -pm0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/


%files
%doc README COPYING changelog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
%autochangelog
