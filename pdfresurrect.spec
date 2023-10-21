Name:		pdfresurrect
Version:	0.23
Release:	%autorelease
Summary:	PDF Analysis and Scrubbing Utility
License:	GPL-3.0-or-later
URL:		https://github.com/enferex/%{name}
Source0:	https://github.com/enferex/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		pdfresurrect-0001-Don-t-reset-compiler-s-flags-during-checks.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	make


%description
PDFResurrect is a tool aimed at analyzing PDF documents. The PDF format
allows for previous document changes to be retained in a more recent
version of the document, thereby creating a running history of changes
for the document. This tool attempts to extract all previous versions
while also producing a summary of changes between versions. This tool
can also "scrub" or write data over the original instances of PDF objects
that have been modified or deleted, in an effort to disguise information
from previous versions that might not be intended for anyone else to read.


%prep
%autosetup -p 1


%build
autoreconf -ivf
%configure
make %{?_smp_mflags}


%install
%make_install

%files
%license LICENSE
%doc AUTHORS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*


%changelog
%autochangelog
