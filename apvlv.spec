%global debug_package %{nil}

Name:           apvlv
Version:        0.5.0
Release:        %autorelease
Summary:        PDF viewer which behaves like Vim
License:        GPLv2+
URL:            https://github.com/naihe2010/apvlv
Source0:        https://github.com/downloads/naihe2010/apvlv/apvlv-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  ebook-tools-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gtk3-devel
BuildRequires:  man-db
BuildRequires:  poppler-glib-devel
BuildRequires:  webkit2gtk3-devel

%description
apvlv is a GTK2 PDF and DjVu viewer with a vim look-and-feel.
It can also browse through directories of such documents.

%prep
%autosetup -p 1

%build
# umd.h is missing to enable the following:
# -DAPVLV_WITH_UMD:BOOL=ON 
# Does not compile with the following option:
# -DAPVLV_WITH_HTML:BOOL=ON

export LDFLAGS="-fPIE"
%cmake . -DDOCDIR=%{_pkgdocdir} -DAPVLV_WITH_DJVU:BOOL=ON -DAPVLV_WITH_TXT:BOOL=ON
%cmake_build

%install
%cmake_install
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE1}

%files
%doc TODO NEWS
%doc AUTHORS THANKS
%doc %{_pkgdocdir}/*
%{_bindir}/apvlv
%{_datadir}/applications/%{name}.desktop
%{_mandir}/apvlv.1
%config(noreplace)%{_sysconfdir}/apvlvrc

%changelog
%autochangelog
