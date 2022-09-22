Version: 2.000
Release: %autorelease
URL:     https://software.sil.org/lateef/

%global foundry           SIL
%global fontlicense       OFL

%global fontlicenses      OFL.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global fontfamily        lateef
%global fontsummary       An Arabic script unicode font
%global fontpkgheader     %{expand:
}

%global fonts             *.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Lateef is named after Shah Abdul Lateef Bhitai, the famous Sindhi mystic and
poet. It is intended to be an appropriate style for use in Sindhi and other
languages of the South Asian region.
}

Source0:  https://software.sil.org/downloads/r/lateef/Lateef-%{version}.zip
Source10: 65-%{fontpkgname}.conf

%fontpkg

%package   doc
Summary:   Optional documentation files of %{name}
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with
%{name}.

%prep
%setup -q -n Lateef-%{version}
%linuxtext *.txt

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%files doc
%defattr(644, root, root, 0755)
%license OFL.txt
%doc documentation

%changelog
%autochangelog
