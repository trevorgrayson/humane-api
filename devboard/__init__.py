
#  each feed = a project, should be able to `name:`
#
#  +-proj-----------|-prs-----|-blds-|
#  | ds-py-models   | 1201/57 | pass | https://...
#  | recs-filter    |         | fail |
#  += news =========================================-
#  | OP Ed - Democrats are ruining everything https://wsj.whatever.com
#  | OP Ed - Democrats are ruining everything
#  | OP Ed - Democrats are ruining everything
#  | OP Ed - Democrats are ruining everything
#  | OP Ed - Democrats are ruining everything
#  +-------------------------------------------------------+
#


def main(stdscr):
    # Clear screen
    stdscr.clear()

    # prs
    yours_total = 5
    yours_attn = 2
    all_total = 12
    all_attn = 3
    kratio = round(yours_total/all_total * 100)

    # tc build
    good = 10
    err = 2
    warning = 3

    # PRs [@{needs_attention}/t{your_total} @{prs_for_your_attention}/t{outstanding_prs}
    stdscr.addstr(0, 0, "@%s/%s @%s/%s %s%% " %(yours_attn, yours_total, all_attn, all_total, kratio))
    # NEEDS_@TTENTION/TOTAL_PRs_YOU_OPEN NEEDS_@TTENTION/TOTAL_PRs kr:KARMA_RATIO%
    stdscr.addstr(0, 17, " bld e%s/w%s/%s %s%% " %(good, err, warning, round(100*err/(good+err))))
    # todo links
    stdscr.addstr(0, 38, "|ghub1 |ghub2 |tc1 |tc2 |tc3 |email")
    stdscr.addstr(1, 0, "ml:what is the status? sg:here is that @emails.txt")
    # stdscr.addstr(10, 0, "+--------------+")
    # stdscr.addstr(4, 0, "+------------------+")
    # METAR
    stdscr.refresh()
    stdscr.getkey()
    # print once and quit like magic fortune when shell opens
    # could also flash it once every egg clock timer style mintes, when cmd is run.
