%global git_commit 29590a6719c725bc95730e72213a00ef92cfa489
%global git_date 20250901

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:		morserunner
Version:	1.68z^%{git_suffix}
Release:	1%{?dist}
Summary:	Amateur radio morse code contest simulator
License:	MPL-2.0
URL:		https://github.com/zmetzing/MorseRunner
Source0:	%{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Source1:	morserunner.desktop
Source2:	LICENSE.md
BuildRequires:	make
BuildRequires:	lazarus-tools
BuildRequires:	lazarus-lcl-gtk2
BuildRequires:	dos2unix
BuildRequires:	sdl12-compat-devel
BuildRequires:	ImageMagick
BuildRequires:	desktop-file-utils
Requires:	hicolor-icon-theme
# It seems lazarus isn't avalable on s390x
ExcludeArch:	s390x
Patch:		morserunner-1.68z-linux-dirs.patch

%description
Amateur radio morse code contest simulator.

%prep
%setup -q -n MorseRunner-%{git_commit}

cp %{SOURCE2} .

# Fix line endings
dos2unix *.{pas,dpr,lpr,txt,dfm,lfm} VCL/*.pas

%autopatch -p1

%build
%make_build

# Icon
convert -set filename:dim '%%wx%%h' ./MorseRunner.ico morserunner-%%[filename:dim].png
for res in 16 32
do
  mkdir -p hicolor/${res}x${res}/apps
  cp morserunner-${res}x${res}.png hicolor/${res}x${res}/apps/morserunner.png
done
rm morserunner-*.png

%install
install -Dpm755 lib/*/MorseRunner %{buildroot}%{_bindir}/MorseRunner
install -Dpm644 Master.dta %{buildroot}%{_datadir}/morserunner/Master.dta

# Install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
cp -r hicolor/* %{buildroot}%{_datadir}/icons/hicolor/

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

%files
%license LICENSE.md
%doc Readme.txt
%{_bindir}/MorseRunner
%{_datadir}/morserunner
%{_datadir}/applications/morserunner.desktop
%{_datadir}/icons/hicolor/*/apps/morserunner.png

%changelog
* Mon Sep 01 2025 Jaroslav Škarvada <jskarvad@redhat.com> - 1.68z^20250901git29590a67-1
- Initial version
