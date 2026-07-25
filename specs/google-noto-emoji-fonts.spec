# SPDX-License-Identifier: MIT

%global commit0 8998f5dd683424a73e2314a8c1f1e359c19e8742
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global fontname google-noto-emoji

# The font build process need to download the code from the internet,
# skip to build the font.
%global buildfont 0

BuildRequires:  gcc
BuildRequires:  fontpackages-devel
%if %buildfont
BuildRequires:  fonttools
BuildRequires:  python3-fonttools
BuildRequires:  nototools
BuildRequires:  python3-nototools
BuildRequires:  python3-devel
BuildRequires:  GraphicsMagick
BuildRequires:  pngquant
BuildRequires:  zopfli
BuildRequires:  cairo-devel
%endif
BuildRequires:  make

Version: 20260526
Release: %autorelease
URL:     https://github.com/googlefonts/noto-emoji

%global foundry           Google
# In noto-emoji-fonts source
## noto-emoji code is in ASL 2.0 license
## Emoji fonts are under OFL license
### third_party color-emoji code is in BSD license
### third_party region-flags code is in Public Domain license
# In nototools source
## nototools code is in ASL 2.0 license
### third_party ucd code is in Unicode license
%global fontlicense       OFL-1.1 AND Apache-2.0
%global fontlicenses      LICENSE OFL.txt
%global fontdocs          AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md README.txt

%global fontfamily0       Noto Emoji
%global fontsummary0      Google “Noto Emoji” Black-and-White emoji font
%global fonts0            NotoEmoji-Regular.ttf
%global fontdescription0  %{expand:
This package provides the Google “Noto Emoji” Black-and-White emoji font.
}

%global fontfamily1       Noto Color Emoji
%global fontsummary1      Google “Noto Color Emoji” colored emoji font
%global fontpkgheader1    %{expand:
Obsoletes:      google-noto-emoji-color-fonts < 20220916-6
Provides:       google-noto-emoji-color-fonts = %{version}-%{release}
}
%global fonts1            Noto-COLRv1.ttf
%global fontdescription1  %{expand:
This package provides the Google “Noto Color Emoji” colored emoji font.
}

%global fontfamily2       Noto Emoji VF
%global fontsummary2      Google “Noto Emoji” Black-and-White emoji variable font
%global fonts2            NotoEmoji-VariableFont_wght.ttf
%global fontdescription2  %{expand:
This package provides the Google “Noto Emoji” Black-and-White emoji variable font.
}

Source0:        https://github.com/googlefonts/noto-emoji/archive/%{commit0}.tar.gz#/noto-emoji-%{shortcommit0}.tar.gz
Source4:        Noto_Emoji.zip


%fontpkg -a


%prep
%autosetup -p1 -a 4 -n noto-emoji-%{commit0}

rm -rf third_party/pngquant

cp -p static/NotoEmoji-Regular.ttf .

%build

%if %buildfont
# Work around UTF-8
export LANG=C.UTF-8

%make_build OPT_CFLAGS="$RPM_OPT_FLAGS" BYPASS_SEQUENCE_CHECK='True'
%else
cp -p fonts/Noto-COLRv1.ttf .
%endif

%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a


%changelog
%autochangelog
