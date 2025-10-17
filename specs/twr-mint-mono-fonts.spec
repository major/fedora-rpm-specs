# Packaging template: multi-family fonts packaging.
#
# SPDX-License-Identifier: MIT
#
# This template documents spec declarations, used when packaging multiple font
# families, from a single dedicated source archive. The source rpm is named
# after the first (main) font family). Look up “fonts-3-sub” when the source
# rpm needs to be named some other way.
#
# It is part of the following set of packaging templates:
# “fonts-0-simple”: basic single-family fonts packaging
# “fonts-1-full”:   less common patterns for single-family fonts packaging
# “fonts-2-multi”:  multi-family fonts packaging
# “fonts-3-sub”:    packaging fonts, released as part of something else
#
Version: 0.0.1
Release: %autorelease
URL:     https://github.com/yuru7/mint-mono/
BuildRequires: fonts-rpm-macros >= 1:2.0.5-9


# The following declarations will be aliased to [variable]0 and reused for all
# generated *-fonts packages unless overriden by a specific [variable][number]
# declaration.
%global foundry           TWR
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE
%global fontdocs          %{nil}
%global fontdocsex        %{fontlicenses}

# A text block that can be reused as part of the description of each generated
# subpackage.
%global common_description %{expand:
Mint Mono is designed for programming which is based on Intel One Mono
and Circle M+.
}

# Declaration for the subpackage containing the first font family. Also used as
# source rpm info. All the [variable]0 declarations are equivalent and aliased
# to [variable].




%global fontfamily0       Mint Mono
%global fontsummary0      Mint Mono, monospace typeface TrueType font
%global fontpkgheader0    %{expand:
}
%global fonts0            MintMono/MintMono-Regular.ttf MintMono/MintMono-Italic.ttf MintMono/MintMono-BoldItalic.ttf MintMono/MintMono-Bold.ttf
%global fontsex0          %{nil}
%global fontconfs0        %{SOURCE11}
%global fontconfsex0      %{nil}
%global fontdescription0  %{expand:
%{common_description}
This package contains Mint Mono which is a monospace typeface of TrueType font.
}



%global fontfamily1       Mint Mono 35
%global fontsummary1      Mint Mono 35, monospace typeface TrueType font
%global fontpkgheader1    %{expand:
}
%global fonts1            MintMono35/MintMono35-Regular.ttf MintMono35/MintMono35-Italic.ttf MintMono35/MintMono35-BoldItalic.ttf MintMono35/MintMono35-Bold.ttf
%global fontsex1          %{nil}
%global fontconfs1        %{SOURCE12}
%global fontconfsex1      %{nil}
%global fontdescription1  %{expand:
%{common_description}
This package contains Mint Mono 35 which is a monospace typeface of TrueType font.
}



Source0:  https://github.com/yuru7/mint-mono/releases/download/v%{version}/MintMono_v%{version}.zip
Source1:  https://raw.githubusercontent.com/yuru7/mint-mono/refs/heads/main/LICENSE
Source11: 69-twr-mint-mono-fonts.conf
Source12: 69-twr-mint-mono-35-fonts.conf

# “fontpkg” will generate the font subpackage headers corresponding to the
# elements declared above.
# “fontpkg” accepts the following selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontpkg -a

# “fontmetapkg” will generate a font meta(sub)package header for all the font
# subpackages generated in this spec. Optional arguments:
# – “-n [name]”      use [name] as metapackage name
# – “-s [variable]”  use the content of [variable] as metapackage summary
# – “-d [variable]”  use the content of [variable] as metapackage description
# – “-z [numbers]”   restrict metapackaging to [numbers] comma-separated list
#                    of font package suffixes
%fontmetapkg

%prep
%setup -q -n MintMono_v0.0.1
cp %{SOURCE1} .

%build
# “fontbuild” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontbuild -a

%install
# “fontinstall” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontinstall -a

%check
# “fontcheck” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontcheck -a

# “fontfiles” accepts the usual selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block
%fontfiles -a

%changelog
%autochangelog
