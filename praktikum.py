from ai_pkg.planning import PlanningProblem, Action, goal_test
from ai_pkg.utils import expr

def double_tennis_problem():
    initial = 'At(A, LeftBaseLine) & At(B, RightNet) & Approaching(Ball, RightBaseLine) & Team(A, B) & Team(B, A)'

    goal = 'Returned(Ball) & At(a, LeftNet) & At(b, LeftNet)'

    action = [
        Action('Hit(player, Ball, loc)',
               precond='Approaching(Ball, loc) & At(player, loc)',
               effect='Returned(Ball)'),
        
        Action('Go(player, to, loc)',
               precond='At(player, loc)',
               effect='At(player, to)'),
        
        Action('NoOp(player)',
               precond='',
               effect='')
    ]

    return PlanningProblem(init=initial, goals=goal, actions=action)

if __name__ == '__main__':
    p = double_tennis_problem()
    print(goal_test(p.goals, p.init))

    solution = [
        expr("Go(A, LeftNet, LeftBaseLine)"),
        expr("NoOp(A)"),
        expr("Go(B, RightBaseLine, RightNet)"),
        expr("Hit(B, Ball, RightBaseLine)")
    ]
    
    for action in solution:
        p.act(action)
    
    print(goal_test(p.goals, p.init))