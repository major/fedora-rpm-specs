%global         altname         Aegisub

Name:           aegisub
Version:        3.4.2
Release:        %autorelease
Summary:        Tool for creating and modifying subtitles
License:        BSD-3-Clause AND ISC AND MIT
# BSD-3-Clause license except the following file:
# ISC:
# ./tools/*
# ./tests/*
# ./libaegisub/* except the following BSD-3-Clause:
# - ./libaegisub/common/cajun/{elements,reader}.cpp
# - ./libaegisub/include/libaegisub/cajun/{elements,reader,visitor}.h
# - ./libaegisub/include/lagi_pre(_c).h
# ./automation/autoload/select-overlaps.moon
# ./automation/autoload/strip-tags.lua
# ./automation/include/aegisub/* except ../unicode.moon BSD-3-Clause
# ./automation/include/clipboard.lua
# ./automation/include/re.lua
# ./automation/include/unicode.lua
# ./automation/tests/aegisub.cpp
# ./automation/tests/modules/*
# ./src/ass_attachment.cpp
# ./src/ass_attachment.h
# ./src/ass_entry.cpp
# ./src/ass_file.cpp
# ./src/ass_info.h
# ./src/ass_karaoke.cpp
# ./src/ass_karaoke.h
# ./src/ass_parser.cpp
# ./src/ass_parser.h
# ./src/async_video_provider.cpp
# ./src/async_video_provider.h
# ./src/audio_karaoke.cpp
# ./src/audio_karaoke.h
# ./src/audio_marker.cpp
# ./src/audio_marker.h
# ./src/audio_provider_factory.cpp
# ./src/audio_provider_factory.h
# ./src/audio_timing_karaoke.cpp
# ./src/colour_button.cpp
# ./src/colour_button.h
# ./src/command/command.cpp
# ./src/command/command.h
# ./src/command/vis_tool.cpp
# ./src/compat.cpp
# ./src/compat.h
# ./src/context.cpp
# ./src/crash_writer_minidump.cpp
# ./src/crash_writer.cpp
# ./src/crash_writer.h
# ./src/dialog_autosave.cpp
# ./src/dialog_dummy_video.cpp
# ./src/dialog_export_ebu3264.cpp
# ./src/dialog_export_ebu3264.h
# ./src/dialog_fonts_collector.cpp
# ./src/dialog_manager.h
# ./src/dialog_progress.cpp
# ./src/dialog_progress.h
# ./src/dialog_resample.cpp
# ./src/dialog_search_replace.cpp
# ./src/dialog_search_replace.h
# ./src/dialog_selected_choices.cpp
# ./src/dialog_selection.cpp
# ./src/dialog_shift_times.cpp
# ./src/dialog_spellchecker.cpp
# ./src/dialog_styling_assistant.cpp
# ./src/dialog_styling_assistant.h
# ./src/dialog_translation.cpp
# ./src/dialog_translation.h
# ./src/dialog_video_properties.cpp
# ./src/dialogs.h
# ./src/factory_manager.h
# ./src/flyweight_hash.h
# ./src/font_file_lister_coretext.mm
# ./src/font_file_lister_fontconfig.cpp
# ./src/font_file_lister_gdi.cpp
# ./src/font_file_lister.cpp
# ./src/font_file_lister.h
# ./src/format.h
# ./src/gl_wrap.cpp
# ./src/gl_wrap.h
# ./src/grid_column.cpp
# ./src/grid_column.h
# ./src/hotkey_data_view_model.cpp
# ./src/hotkey_data_view_model.h
# ./src/hotkey.cpp
# ./src/include/aegisub/context.h
# ./src/include/aegisub/hotkey.h
# ./src/include/aegisub/menu.h
# ./src/include/aegisub/spellchecker.h
# ./src/include/aegisub/toolbar.h
# ./src/initial_line_state.cpp
# ./src/initial_line_state.h
# ./src/libass_gdi_fontselect.cpp
# ./src/libresrc/libresrc.cpp
# ./src/libresrc/libresrc.h
# ./src/menu.cpp
# ./src/mkv_wrap.h
# ./src/options.h
# ./src/osx/osx_utils.mm
# ./src/osx/retina_helper.mm
# ./src/pen.cpp
# ./src/pen.h
# ./src/persist_location.cpp
# ./src/persist_location.h
# ./src/placeholder_ctrl.h
# ./src/preferences_base.cpp
# ./src/preferences_base.h
# ./src/preferences.cpp
# ./src/preferences.h
# ./src/project.cpp
# ./src/project.h
# ./src/res/res.rc
# ./src/res/strings_utf8.rc
# ./src/res/strings.rc
# ./src/resolution_resampler.cpp
# ./src/resolution_resampler.h
# ./src/retina_helper.h
# ./src/search_replace_engine.cpp
# ./src/search_replace_engine.h
# ./src/selection_controller.cpp
# ./src/spellchecker_hunspell.cpp
# ./src/spellchecker_hunspell.h
# ./src/spellchecker.cpp
# ./src/subs_controller.cpp
# ./src/subs_controller.h
# ./src/subtitle_format_ass.cpp
# ./src/subtitle_format_ass.h
# ./src/subtitle_format_ebu3264.cpp
# ./src/subtitle_format_ebu3264.h
# ./src/subtitle_format_ssa.cpp
# ./src/subtitle_format_ssa.h
# ./src/subtitles_provider_csri.h
# ./src/subtitles_provider_libass.h
# ./src/subtitles_provider.cpp
# ./src/text_file_reader.cpp
# ./src/text_file_reader.h
# ./src/text_file_writer.cpp
# ./src/text_file_writer.h
# ./src/text_selection_controller.cpp
# ./src/text_selection_controller.h
# ./src/thesaurus.cpp
# ./src/thesaurus.h
# ./src/toolbar.cpp
# ./src/validators.cpp
# ./src/validators.h
# ./src/value_event.h
# ./src/vector2d.cpp
# ./src/vector2d.h
# ./src/video_frame.cpp
# ./src/video_frame.h
# ./src/video_out_gl.cpp
# ./src/video_out_gl.h
# ./src/video_provider_cache.cpp
# ./src/video_provider_manager.cpp
# ./src/video_provider_manager.h
# ./src/visual_tool_clip.cpp
# ./src/visual_tool_clip.h
# ./src/visual_tool_cross.cpp
# ./src/visual_tool_cross.h
# ./src/visual_tool_drag.cpp
# ./src/visual_tool_drag.h
# ./src/visual_tool_rotatexy.cpp
# ./src/visual_tool_rotatexy.h
# ./src/visual_tool_rotatez.cpp
# ./src/visual_tool_rotatez.h
# ./src/visual_tool_scale.cpp
# ./src/visual_tool_scale.h
# ./src/visual_tool_vector_clip.cpp
# ./src/visual_tool_vector_clip.h
# ./src/visual_tool.cpp
# ./src/visual_tool.h
#
# MIT:
# ./subprojects/luabins/
# ./libaegisub/lua/modules/lpeg.{c,h}
# ./automation/include/cleantags.lua
# ./automation/autoload/cleantags-autoload.lua
#
# Khronos License:
# ./src/gl/glext.h
#
# Licensed to BSDL with permission from the author:
# ./src/MatroskaParser.{c,h}

URL:            https://github.com/TypesettingTools/%{name}

Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# https://github.com/TypesettingTools/Aegisub/pull/375
Patch1:         0001-fix-Fallback-to-X11-if-lacks-EGL-support.patch

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  wxGTK-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(uchardet)

Requires: hicolor-icon-theme

# Heavily modified upon the original project
Provides: bundled(cajun-jsonapi) = 2.0.1
# Major ABI change making patching out impossible
Provides: bundled(lua-lpeg) = 0.1.0
# Discontinued project, not included in Fedora Package registry
Provides: bundled(lua-luabins) = 0.3

%description
Aegisub is an advanced subtitle editor which assists in the creation of
subtitles, timing, and editing of subtitle files. It supports a wide range
of formats and provides powerful visual typesetting tools.

%prep
%autosetup -n %{altname}-%{version} -p1

# Strip out unused bundled library
find subprojects/ -mindepth 1 -depth ! -path "subprojects/luabins*" -exec rm -rv {} +
# Bundled: src/gl/glext.h (Provided by `libglvnd-devel`, unable to patch out due to upstream cross-platform modification)
# Strip unused packaging artifacts for other platform, which contains GPL code
rm -rv packages/{osx_bundle,osx_dmg,win_installer}
rm -rv tools/{osx-*,apply-manifest.py,*.ps1}
rm -rv osx-bundle.sed
# ./docs consists of project related document and tools, but not application manual
rm -rv docs/

%build
%meson -Denable_update_checker=false
%meson_build

%install
%meson_install

%check
%meson_test

%find_lang %{name}

desktop-file-validate %{buildroot}%{_datadir}/applications/org.%{name}.%{altname}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.%{name}.%{altname}.metainfo.xml

%files -f %{name}.lang
%{_datadir}/applications/org.%{name}.%{altname}.desktop
%{_metainfodir}/org.%{name}.%{altname}.metainfo.xml
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.%{name}.%{altname}.*
%license LICENCE

%changelog
%autochangelog
